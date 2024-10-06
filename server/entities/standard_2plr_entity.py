from pydantic import BaseModel

class Standard2PlrStreakCreate(BaseModel):
    length: int
    player1: str
    player2: str
    player1_character: str
    player2_character: str
    player1_stocks: int
    player2_stocks: int
    player1_deaths: int
    player2_deaths: int
    player1_1v1_clutches: int
    player2_1v1_clutches: int
    player1_1v2_clutches: int
    player2_1v2_clutches: int
    date: str
    duration: float
    concluded: bool
    #TODO: add stage list
