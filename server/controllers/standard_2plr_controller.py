from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import database, standard_2plr_model
from ..schemas.standard_2plr_entity import Standard2PlrStreakCreate

router = APIRouter()

@router.post("/standard-2plr-streaks")
async def create_standard_2plr_streak(
    match_data: Standard2PlrStreakCreate,
    db: Session = Depends(database.get_db)
):
    match = standard_2plr_model.Standard2PlrStreak(**match_data.model_dump())
    db.add(match)
    db.commit()
    db.refresh(match)
    return match

@router.put("/standard-2plr-streaks/{id}")
async def update_standard_2plr_streak(
    id: int,
    match_data: Standard2PlrStreakCreate,
    db: Session = Depends(database.get_db)
):
    match = db.query(standard_2plr_model.Standard2PlrStreak).filter(standard_2plr_model.Standard2PlrStreak.id == id).first()
    
    if match is None:
        raise HTTPException(status_code=404, detail="Streak not found")
    
    for key, value in match_data.model_dump().items():
        setattr(match, key, value)
    
    db.commit()
    db.refresh(match)
    return match
    
@router.get("/standard-2plr-streaks")
async def get_standard_2plr_streaks(db: Session = Depends(database.get_db)):
    return db.query(standard_2plr_model.Standard2PlrStreak).all()

@router.get("/standard-2plr-streaks/{id}")
async def get_standard_2plr_streak(id: int, db: Session = Depends(database.get_db)):
    return db.query(standard_2plr_model.Standard2PlrStreak).filter(standard_2plr_model.Standard2PlrStreak.id == id).first()
