from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Standard2PlrStreak(Base):
    __tablename__ = "standard_2plr_streaks"

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    player1 = Column(String)
    player2 = Column(String)
    player1_character = Column(String)
    player2_character = Column(String)
    player1_kills = Column(Integer)
    player2_kills = Column(Integer)
    player1_deaths = Column(Integer)
    player2_deaths = Column(Integer)
    player1_1v1_clutches = Column(Integer)
    player2_1v1_clutches = Column(Integer)
    player1_1v2_clutches = Column(Integer)
    player2_1v2_clutches = Column(Integer)
    date = Column(String)
    duration = Column(Float)
    concluded = Column(Boolean)
    #TODO: add stage list