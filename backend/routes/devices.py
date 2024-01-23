from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session

from schemas import device_schema
from database import get_db
from repositories import device_repo

router = APIRouter()

@router.get("/devices", tags=["Devices"], response_model=List[device_schema.Device])
async def get_all_devices(name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get all the Devices stored in database
    """
    if name:
        devices =[]
        db_device = device_repo.fetch_by_name(db,name)
        devices.append(db_device)
        return devices
    else:
        return device_repo.DeviceRepo.fetch_all(db)
    

@router.get('/device/{no_device}', tags=["Device"],response_model=device_schema.Device)
async def get_device(no_device: int, db: Session = Depends(get_db)):
    """
    Get the Device with the given no_device provided by User stored in database
    """
    db_item = device_repo.DeviceRepo.fetch_by_no_device(db, no_device)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given no_device")
    return db_item