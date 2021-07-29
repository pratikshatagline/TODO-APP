from typing import List,Optional
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str

class ShowTodo(BaseModel):
    title : str
    description: str
    
    class Config():
        orm_mode = True
 