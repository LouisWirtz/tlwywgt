from sqlalchemy.orm import Session

from . import models, schemas


def get_idea(db: Session, idea_id: int):
    """Method for getting a idea by its id."""
    return db.query(models.Idea).filter(models.Idea.id == idea_id).first()


def get_idea_by_title(db:Session, idea_title: str):
    """Method for getting a idea by its title."""
    return db.query(models.Idea).filter(models.Idea.title == idea_title).first()


def get_ideas(db: Session, skip: int = 0, limit: int = 100):
    """Method to read multiple ideas."""
    return db.query(models.Idea).offset(skip).limit(limit).all()


def create_idea(db: Session, idea: schemas.IdeaCreate, idea_id: int):
    """Method to create one idea."""
    db_idea = models.Idea(**idea.dict(), owner_id=idea_id)
    db.add(db_idea)
    db.commit()
    db.refresh(db_idea)
    return db_idea
