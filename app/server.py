from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from langserve import add_routes

from app.custom_model import CustomLLM

app = FastAPI()

sugma=CustomLLM(n=2)
sugma.invoke("help")
sugma.invoke([HumanMessage("help")])
add_routes(app, CustomLLM(n=2))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
