from fastapi import APIRouter
from app.schemas import CreateTask
from app.schemas import UpdateTask

task_router = APIRouter(prefix="/task", tags=["task"])


@task_router.get("/")
async def all_task():
    pass


@task_router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass


@task_router.post("/create")
async def create_task(task: CreateTask):
    pass


@task_router.put("/update")
async def update_task(task_id: int, task: UpdateTask):
    pass


@task_router.delete("/delete")
async def delete_task(task_id: int):
    pass
