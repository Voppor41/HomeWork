from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users_db = {"1": "Имя: Example, возраст: 19"}

@app.get("/users")
async def get_all_users() -> dict:
    return users_db

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=2, max_length=10, description="Enter your username", example="Lee")],
                      age: int=Path(ge=18, le=60, description="Enter your age", example="20")) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"

@app.put("/user/{user_id},/{username}/{age}")
async def update_db(user_id: str, username: str, age: int) -> str:
    users_db[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    users_db.pop(user_id)
    return f"The user {user_id} is deleted"