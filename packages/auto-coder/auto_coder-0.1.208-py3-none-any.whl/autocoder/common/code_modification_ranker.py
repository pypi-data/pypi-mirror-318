import byzerllm
from typing import List,Union
from autocoder.common import AutoCoderArgs
from autocoder.common.types import CodeGenerateResult
from pydantic import BaseModel
from loguru import logger
from concurrent.futures import ThreadPoolExecutor, as_completed
import traceback

class RankResult(BaseModel):
    rank_result:List[int]

class CodeModificationRanker:
    def __init__(self, llm: byzerllm.ByzerLLM, args: AutoCoderArgs):
        self.llm = llm
        self.args = args     
        if self.llm.get_sub_client("generate_rerank_model"):
            self.rerank_llm = self.llm.get_sub_client("generate_rerank_model")
        else:
            self.rerank_llm = self.llm
    
    @byzerllm.prompt()
    def _rank_modifications(self, s:CodeGenerateResult) -> str:
        '''
        对一组代码修改进行质量评估并排序。

        下面是修改需求：
        
        <edit_requirement>
        {{ s.conversations[0][-2]["content"] }}
        </edit_requirement>
        
        下面是相应的代码修改：
        {% for content in s.contents %}
        <edit_block id="{{ loop.index0 }}">
        {{content}}
        </edit_block>
        {% endfor %}
        
        请输出如下格式的评估结果,只包含 JSON 数据:

        ```json
        {
            "rank_result": [id1, id2, id3]  // id 为 edit_block 的 id,按质量从高到低排序
        }
        ```

        注意，只输出前面要求的 Json 格式就好，不要输出其他内容，Json 需要使用 ```json ```包裹。
        '''
        

    def rank_modifications(self, generate_result: CodeGenerateResult) -> CodeGenerateResult:
        import time
        start_time = time.time()
        
        # 如果只有一个候选，直接返回
        if len(generate_result.contents) == 1:
            logger.info("Only 1 candidate, skip ranking")
            return generate_result
            
        logger.info(f"Start ranking {len(generate_result.contents)} candidates")
        generate_times = self.args.generate_times_same_model
        
        try:
            # Create a thread pool with generate_times workers
            with ThreadPoolExecutor(max_workers=generate_times) as executor:
                # Submit tasks
                futures = [
                    executor.submit(
                        self._rank_modifications.with_llm(self.rerank_llm).with_return_type(RankResult).run,
                        generate_result
                    ) for _ in range(generate_times)
                ]
                
                # Process results as they complete
                for future in as_completed(futures):
                    try:
                        v = future.result()
                        # If we get a valid result, use it and cancel other tasks
                        for f in futures:
                            f.cancel()
                            
                        elapsed = time.time() - start_time
                        logger.info(f"Ranking completed in {elapsed:.2f}s, best candidate index: {v.rank_result[0]}")
                        
                        rerank_contents = [generate_result.contents[i] for i in v.rank_result]
                        rerank_conversations = [generate_result.conversations[i] for i in v.rank_result]
                        return CodeGenerateResult(contents=rerank_contents,conversations=rerank_conversations)
                    except Exception as e:
                        logger.warning(f"Ranking request failed: {str(e)}")
                        logger.debug(traceback.format_exc())
                        continue
        except Exception as e:
            logger.error(f"Ranking process failed: {str(e)}")
            logger.debug(traceback.format_exc())
        
        # If all requests failed, use the original codes
        elapsed = time.time() - start_time
        logger.warning(f"All ranking requests failed in {elapsed:.2f}s, using original order")
        return generate_result
