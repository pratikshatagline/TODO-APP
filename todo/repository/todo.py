from sqlalchemy.orm import Session
from .. import schemas, database, models
from fastapi import APIRouter, Depends, status, Response, HTTPException



def get_all(db: Session):
    todo = db.query(models.Todo).all()
    return todo

def create_all(request:schemas.Todo, db: Session):
    new_todo = models.Todo(title=request.title, description=request.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def destroy_all(id, db:Session):
    db.query(models.Todo).filter(models.Todo.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_all(id, request: schemas.Todo, db:Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail = f" id {id} not found")
    todo.update({'title':request.title, 'description':request.description})
    db.commit()
    return "updated"

def get_one(id, request: schemas.Todo,db:Session):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail = f"id {id} not found")
    return todo
