from datetime import datetime
from pydantic import BaseModel, field_validator


class TaskBase(BaseModel):
    id: str
    name: str
    description: str
    deadline: str
    category: str


class TaskResponse(TaskBase):
    class Config:
        from_attributes = True

    @field_validator('deadline', mode='before')
    @classmethod
    def convert_date(cls, v):
        if v:
            return str(v)


class TaskCreate(TaskBase):
    deadline: datetime

class TaskUpdate(TaskBase):
    ...