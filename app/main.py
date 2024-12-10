from fastapi import FastAPI
from app.models import User
from routers.task import task_router
from routers.user import user_router
import uvicorn
from .backend.db import Base, engine, SessionLocal

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task_router)
app.include_router(user_router)

db = SessionLocal()
new_user = User(username="user1", firstname="John", lastname="Doe", age=30)
db.add(new_user)
db.commit()
db.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
