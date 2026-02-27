from fastapi import FastAPI
from models import Feedback

app = FastAPI()

message = Feedback(name="Сергей", message="У Алёны очень много сваги!!!")
all_feedback = []


@app.post("/feedback")
async def feedback(feedback: Feedback):
    try:
        all_feedback.append(feedback)
        return {"message": f"Спасибо большое за ваш честный и конструктивный отзыв, {feedback.name}!"}
    except ValueError as e:
        return "Вы написали запрещенное слово. Помойте рот с мылом! "