from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from custom_model import CustomLLM

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, CustomLLM(), path="/custom-llm")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
