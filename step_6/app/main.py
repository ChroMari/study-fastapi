from typing import Annotated

from fastapi import FastAPI, Header, Response

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}

# --- Повторяющиеся заголовки
@app.get("/items2/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}


# ---  Доступ к заголовкам запросов
@app.get("/")
def root(user_agent: str = Header()):
    return {"User-Agent": user_agent}


@app.get("/")
def root():
    data = "Hello from here"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123459"})


@app.get("/")
def root(response: Response):
    response.headers["Secret-Code"] = "123459"
    return {"message": "Hello from my api"}