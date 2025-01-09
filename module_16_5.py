from fastapi import FastAPI, Path, Body, HTTPException
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int = 1
    username: str
    age: int


@app.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "users": [user]})


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int) -> str:
    new_id = users[-1].id + 1 if users else 1  # Если список пустой, id = 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_db(user_id: int, username: str, age: int) -> str:
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
def delete_user(user_id: int):
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user)
        return f"The user {user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")