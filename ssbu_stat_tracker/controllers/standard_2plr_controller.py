from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import standard_2plr_match, database
from ..schemas.standard_2plr_match import Standard2PlrMatchCreate

router = APIRouter()

@router.post("/standard-2plr-matches")
async def create_standard_2plr_match(
    match_data: Standard2PlrMatchCreate,
    db: Session = Depends(database.get_db)
):
    match = standard_2plr_match.Standard2PlrMatch(**match_data.model_dump())
    db.add(match)
    db.commit()
    db.refresh(match)
    return match

@router.get("/standard-2plr-matches")
async def get_standard_2plr_matches(db: Session = Depends(database.get_db)):
    return db.query(standard_2plr_match.Standard2PlrMatch).all()
