from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

feedback_bd = []

class Feedback(BaseModel):
    name: str
    message: str


@app.post("/feedback")
async def add_feedback(feedback: Feedback):
    feedback = dict(feedback)
    feedback_bd.append(feedback)
    message = f'Feedback received. Thank you, {feedback["name"]}!'

    return { "message": message}


@app.get("/")
async def all_feedback():
    return feedback_bd
