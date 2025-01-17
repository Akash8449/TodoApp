from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate
from uuid import uuid4

def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        id=str(uuid4()),
        title=task.title,
        description=task.description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session, is_completed: bool | None = None, limit: int = 10, offset: int = 0):
    query = db.query(Task)
    if is_completed is not None:
        query = query.filter(Task.is_completed == is_completed)
    return query.offset(offset).limit(limit).all()

def get_task(db: Session, task_id: str):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: str, task: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return None
    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
