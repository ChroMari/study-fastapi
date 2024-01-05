from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(test: str | None = Cookie(default=None)):
    return {"ads_id": test}
