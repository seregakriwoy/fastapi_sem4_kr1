from fastapi import FastAPI
from models import User

app = FastAPI()
first_user = User(name="Шевалдышев Сергей", age=20)

@app.post("/user")
async def get_user(user: User):
    if user.age < 18:
        is_adult = False
    else:
        is_adult = True
    return {"name": user.name, "age": user.age, "is_adult": is_adult}