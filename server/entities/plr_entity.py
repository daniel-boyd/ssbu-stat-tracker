from pydantic import BaseModel

class PlrCreate(BaseModel):
    name: str
    streaks_played: int
    games_played: int
    kills_total: int
    deaths_total: int
    kd_total: float
    clutches_1v1_total: int
    clutches_1v2_total: int
    longest_streak: int
    longest_streak_character: str
    longest_streak_teammate: str
    longest_streak_teammate_character: str
    longest_streak_date: str