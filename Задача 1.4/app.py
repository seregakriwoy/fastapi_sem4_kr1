from fastapi import FastAPI
from models import User

app = FastAPI()
first_user = User(name="Шевалдышев Сергей", id=1)


@app.get("/user")
async def get_user():
    return first_user
