from typing import List,Optional
from fastapi import FastAPI, Depends, status, HTTPException, Response
from . import models, schemas
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .routers import todo

app = FastAPI()

app.include_router(todo.router)


models.Base.metadata.create_all(engine)


"""def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/todo', status_code= status.HTTP_201_CREATED, tags=['ToDo'])
def create(request:schemas.Todo, db:Session = Depends(get_db)):
    new_todo = models.Todo(title=request.title, description=request.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.delete('/todo/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['ToDo'])
def destroy(id,db: Session = Depends(get_db)):
    db.query(models.Todo).filter(models.Todo.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/todo/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['ToDo'])
def update(id, request: schemas.Todo, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail = f" id {id} not found")
    todo.update({'title':request.title, 'description':request.description})
    db.commit()
    return "updated"



@app.get('/todo', response_model = List[schemas.ShowTodo], tags=['ToDo'])
def all(db: Session=Depends(get_db)):
    todo = db.query(models.Todo).all()
    return todo

@app.get('/todo/{id}', status_code=200, response_model= schemas.ShowTodo, tags=['ToDo'])
def show(id, response:Response, db: Session=Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail = f"id {id} not found")
    return todo

"""