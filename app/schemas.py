from pydantic import BaseModel, Field
from datetime import datetime

class TaskBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: str | None = Field(None, max_length=500)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(None, max_length=100)
    description: str | None = Field(None, max_length=500)
    is_completed: bool | None = None

class TaskResponse(TaskBase):
    id: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        # Updated for Pydantic V2
        from_attributes = True
