from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import crud, schemas

Base.metadata.create_all(bind=engine)
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def db(): 
    d=SessionLocal()
    try: yield d
    finally: d.close()

@app.get("/todos")
def list(db:Session=Depends(db)): return crud.get_all(db)

@app.get("/todos/{id}")
def get(id:int, db:Session=Depends(db)): return crud.get_one(db,id)

@app.post("/todos")
def create(t:schemas.TodoCreate, db:Session=Depends(db)): return crud.create(db,t)

@app.put("/todos/{id}")
def update(id:int,t:schemas.TodoUpdate,db:Session=Depends(db)): return crud.update(db,id,t)

@app.delete("/todos/{id}")
def delete(id:int,db:Session=Depends(db)): return crud.delete(db,id)
