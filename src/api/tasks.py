from datetime import datetime
from sqlalchemy import text, select, func
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from src.schema import TaskResponse, TaskCreate, TaskUpdate
from src.utils.utils import item_to_task
from src.database.session import get_db
from src.models.tasks import Tasks


router = APIRouter(prefix='/tasks')


@router.get("/read_tasks", response_model=list[TaskResponse])
async def read_tasks(db: Session = Depends(get_db)):

    tasks = db.execute(select(Tasks))
    task_rows = tasks.scalars().all()
    return(task_rows)


@router.post("/upgrade_task")
async def upgrade_task(item: TaskUpdate, db: Session = Depends(get_db)):
    task_db = db.execute(select(Tasks).where(Tasks.id == item.id)).scalars().first()
    task_db.name = item.name
    task_db.description = item.description
    task_db.category = item.category
    task_db.deadline = item.deadline

    db.add(task_db)

    db.commit()

    return True


@router.post("/create_task")
async def create_task(item: TaskCreate, db: Session = Depends(get_db)):
    new_task = Tasks(
        **item.model_dump()
    )
    db.add(new_task)
    db.commit()
    return True


@router.delete("/delete_task")
async def delete_task(task_id: str, db: Session = Depends(get_db)):
    to_delete = db.execute(select(Tasks).where(Tasks.id == task_id)).scalars().first()
    db.delete(to_delete)
    db.commit()
    return True
