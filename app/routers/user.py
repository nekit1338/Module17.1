from fastapi import APIRouter
from app.schemas import CreateUser
from app.schemas import UpdateUser

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/")
async def all_users():
    pass


@user_router.get("/{user_id}")
async def user_by_id(user_id):
    pass


@user_router.post("/create")
async def create_user(user: CreateUser):
    pass


@user_router.put("/update")
async def update_user(user_id: int, user: UpdateUser):
    pass


@user_router.delete("/delete")
async def delete_user(user_id: int):
    pass
