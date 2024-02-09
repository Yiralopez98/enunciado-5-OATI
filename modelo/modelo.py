from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    series_directors = relationship("SeriesDirector", back_populates="director")

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    release_date = Column(String(255))
    description = Column(String(255))
    directors = relationship("SeriesDirector", back_populates="series")

class SeriesDirector(Base):
    __tablename__ = 'series_directors'
    series_id = Column(Integer, ForeignKey('series.id'), primary_key=True)
    directors_id = Column(Integer, ForeignKey('directors.id'), primary_key=True)
    series = relationship("Series", back_populates="directors")
    director = relationship("Director", back_populates="series_directors")
