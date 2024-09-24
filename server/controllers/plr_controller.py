from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import database, plr_model
from ..entities.plr_entity import PlrCreate

router = APIRouter()

# Create new player
@router.post("/plr")
async def create_plr(
    plr_data: PlrCreate,
    db: Session = Depends(database.get_db)
):
    plr = plr_model.Plr(**plr_data.model_dump())
    db.add(plr)
    db.commit()
    db.refresh(plr)
    return plr

# Update single plr by name
@router.put("/plr/{name}")
async def update_plr(
    name: str,
    plr_data: PlrCreate,
    db: Session = Depends(database.get_db)
):
    plr = db.query(plr_model.Plr).filter(plr_model.Plr.name == name).first()
    
    if plr is None:
        raise HTTPException(status_code=404, detail="plr not found")
    
    for key, value in plr_data.model_dump().items():
        setattr(plr, key, value)
    
    db.commit()
    db.refresh(plr)
    return plr
    
# Get first num_plrs plrs
@router.get("/plr/top/{num_plrs}")
async def get_plrs(num_plrs: int, db: Session = Depends(database.get_db)):
    return db.query(plr_model.Plr).limit(num_plrs).all()

# Get single plr by name
@router.get("/plr/name/{name}")
async def get_standard_2plr_streak(name: str, db: Session = Depends(database.get_db)):
    return db.query(plr_model.Plr).filter(plr_model.Plr.name == name).first()