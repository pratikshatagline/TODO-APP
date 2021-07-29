from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import todo



router = APIRouter(
    
    prefix='/todo',
    tags=['ToDo']
    
    )

get_db = database.get_db

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request:schemas.Todo, db:Session = Depends(get_db)):
    return todo.create_all(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(get_db)):
    return todo.destroy_all(id,db)
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Todo, db: Session = Depends(get_db)):
    return todo.update_all(id, request,db)



@router.get('/', response_model = List[schemas.ShowTodo])
def all(db: Session=Depends(get_db)):
    return todo.get_all(db)

@router.get('/{id}', status_code=200, response_model= schemas.ShowTodo)
def show(id, response:Response, db: Session=Depends(get_db)):
    return todo.get_one(id, response, db)