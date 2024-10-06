from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Standard2PlrStreak(Base):
    __tablename__ = "standard_2plr_streaks"

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    player1 = Column(String)
    player2 = Column(String)
    player_1_character = Column(String)
    player_2_character = Column(String)
    player_1_stocks = Column(Integer)
    player_2_stocks = Column(Integer)
    player_1_deaths = Column(Integer)
    player_2_deaths = Column(Integer)
    player_1_1v1_clutches = Column(Integer)
    player_2_1v1_clutches = Column(Integer)
    player_1_1v2_clutches = Column(Integer)
    player_2_1v2_clutches = Column(Integer)
    date = Column(String)
    duration = Column(Float)
    concluded = Column(Boolean)
    #TODO: add stage list