from fastapi import FastAPI
from models import User

app = FastAPI()
first_user = User(name="Шевалдышев Сергей", id=1)

users_db = []

@app.post("/users")
async def post_users(user: User):
    users_db.append(user)

@app.get("/user")
async def get_user():
    return users_db
