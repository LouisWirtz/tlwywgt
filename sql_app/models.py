"""Model for database entries."""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary
# from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.orm import relationship

from .database import Base


class Idea(Base):
    """Describes the table for all ideas."""
    __tablename__ = "idea"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(DateTime)
    image = Column(LargeBinary)


# class IdeaPicture(Base, Image):
#     """Idea image model."""
#     __tablename__ = "idea_image"
#
#     idea_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
#     idea = relationship('idea')


