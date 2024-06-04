from app.custom_chat_model import CustomChatModel
from app.custom_model import CustomLLM
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI()

add_routes(app, CustomChatModel(), path="/chat")
add_routes(app, CustomLLM())

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
