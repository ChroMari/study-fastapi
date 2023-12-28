from fastapi import FastAPI
from .models.feedback import Feedback

app = FastAPI()
feedback_db = []

@app.post("/feedback")
async def feedback(user_feedback: Feedback):
    feedback_db.append(user_feedback)
    return {"message": "Feedback received. Thank you, Alice!"}
