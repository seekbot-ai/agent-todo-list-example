from sqlalchemy.orm import Session
from . import models, schemas

def get_all(db:Session): return db.query(models.Todo).all()
def get_one(db:Session,id:int): return db.query(models.Todo).filter(models.Todo.id==id).first()
def create(db:Session,t:schemas.TodoCreate):
    obj=models.Todo(**t.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
def update(db,id,t:schemas.TodoUpdate):
    obj=get_one(db,id); 
    if not obj: return None
    for k,v in t.dict().items(): setattr(obj,k,v)
    db.commit(); return obj
def delete(db,id):
    obj=get_one(db,id); 
    if not obj: return None
    db.delete(obj); db.commit(); return True
