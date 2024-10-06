from sqlalchemy import Column, Integer, String, Tuple, Float
from .database import Base

class Plr(Base):
    __tablename__ = "plr"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    streaks_played = Column(Integer)
    games_played = Column(Integer)
    stocks_total = Column(Integer)
    deaths_total = Column(Integer)
    kd_total = Column(Float)
    clutches_1v1_total = Column(Integer)
    clutches_1v2_total = Column(Integer)
    longest_streak = Column(String)
    longest_streak_character = Column(String)
    longest_streak_teammate = Column(String)
    longest_streak_teammate_character = Column(String)
    longest_streak_date = Column(String)