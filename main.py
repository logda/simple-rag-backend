from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain import PromptTemplate, LLMChain
from langchain_community.llms import Tongyi
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


# 定义请求和响应的数据模型
class QueryRequest(BaseModel):
    prompt: str
    title: str
    content: str


class QueryResponse(BaseModel):
    status: str
    response: str


# 设置 Tongyi LLM 客户端
llm = Tongyi()

# 定义 Prompt 模板
template = """
标题: {title}

正文: {content}

问题: {prompt}

答案:
"""

prompt_template = PromptTemplate(
    input_variables=["title", "content", "prompt"], template=template
)


@app.post("/rag/query", response_model=QueryResponse)
async def rag_query(query: QueryRequest):
    try:
        # 构建 prompt
        full_prompt = prompt_template.format(
            title=query.title, content=query.content, prompt=query.prompt
        )

        # 使用 LangChain 进行问答处理
        llm_chain = LLMChain(prompt=prompt_template, llm=llm)
        response = llm_chain.run(
            title=query.title, content=query.content, prompt=query.prompt
        )

        # 返回响应
        return QueryResponse(status="success", response=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 启动服务器：使用命令 `uvicorn main:app --reload`
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
