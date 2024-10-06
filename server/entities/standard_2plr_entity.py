from pydantic import BaseModel

class Standard2PlrStreakCreate(BaseModel):
    length: int
    player1: str
    player2: str
    player_1_character: str
    player_2_character: str
    player_1_stocks: int
    player_2_stocks: int
    player_1_deaths: int
    player_2_deaths: int
    player_1_1v1_clutches: int
    player_2_1v1_clutches: int
    player_1_1v2_clutches: int
    player_2_1v2_clutches: int
    date: str
    duration: float
    concluded: bool
    #TODO: add stage list
