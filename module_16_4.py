from fastapi import FastAPI, Path, Body, HTTPException
from typing import List

from pydantic import BaseModel

app = FastAPI()

'''users_db = {"1": "Имя: Example, возраст: 19"}'''
users = []

class User(BaseModel):
    id: int = 1
    username: str
    age: int

@app.get("/users")
async def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    new_id = users[-1].id + 1 if users else 1  # Если список пустой, id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_db(user_id: int, username: str, age: int) -> str:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
        return "User updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user)
        return f"The user {user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")