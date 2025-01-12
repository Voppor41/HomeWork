from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import *
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

user_router = APIRouter(prefix="/user", tags=["user", ])


@user_router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id != 0))
    users = result.scalars().all()  # scalars() используется для извлечения объектов
    return users

@user_router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    return user

@user_router.post("/create_user")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                              firstname=create_user.firstname,
                                              lastname=create_user.lastname,
                                              age=create_user.age,
                                              slug=slugify(create_user.username)
    ))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transcription": "Successful"
    }

@user_router.put("/update_user")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User isn't found"
        )

    db.execute(update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                                       lastname=update_user.lastname,
                                                                       age=update_user.age
    ))

    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "User updated successfuly"
    }

@user_router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User isn't found"
        )

    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "User updated successfuly"
    }