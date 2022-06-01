from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """Method to create a dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/ideas/", response_model=schemas.Idea)
def create_user(user: schemas.IdeaCreate, db: Session = Depends(get_db)):
    db_idea = crud.get_idea_by_title(db, "title=idea.title")  # Here hast to be some title=idea.title
    if db_idea:
        raise HTTPException(status_code=400, detail="Title already exists")


@app.get("/users/", response_model=list[schemas.Idea])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ideas = crud.get_ideas(db, skip=skip, limit=limit)
    return ideas

