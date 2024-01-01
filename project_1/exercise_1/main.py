from fastapi import FastAPI
from fastapi.responses import FileResponse

file_index_path = "index_task_2.html"
app = FastAPI()


@app.get("/")
async def root():
    return FileResponse(file_index_path)
