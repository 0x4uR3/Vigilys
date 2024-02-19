from sqlalchemy.orm import Session

from backend.models import device_model
from backend.schemas import device_schema

class DeviceRepo:
    async def create(db: Session, device: device_schema.DeviceCreate):
        db_device = device_model.Devices(no_device=device.no_device,
                                         nwk_addr=device.nwk_addr,
                                         model_id=device.model_id,
                                         ieee_addr=device.ieee_addr,
                                         location=device.location,
                                         alive=device.alive,
                                         no_parent=device.no_parent,
                                         device_type=device.device_type,
                                         report=device.report,
                                         reportbis=device.reportbis,
                                         unit=device.unit,
                                         unitbis=device.unitbis,
                                         room=device.room,
                                         manuf_code=device.manuf_code,
                                         app_version=device.app_version,
                                         residence=device.residence,
                                         category=device.category,
                                         stack_version=device.stack_version,
                                         last_report=device.last_report,
                                         hw_version=device.hw_version,
                                         zcl_version=device.zcl_version,
                                         date_code=device.date_code,
                                         theme=device.theme,
                                         icone=device.icone,
                                         zone_type=device.zone_type,
                                         device_id=device.device_id)
        db.add(db_device)
        db.commit()
        db.refresh(db_device)
        return db_device

    def fetch_by_no_device(db: Session, no_device):
        return db.query(device_model.Devices).filter(device_model.Devices.no_device == no_device).first()

    def fetch_by_location(db: Session, location):
        return db.query(device_model.Devices).filter(device_model.Devices.location == location).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(device_model.Devices).offset(skip).limit(limit).all()

    async def delete(db: Session, no_device):
        db_device= db.query(device_model.Devices).filter_by(no_device=no_device).first()
        db.delete(db_device)
        db.commit()
        
    async def update(db: Session, device_data):
        updated_device = db.merge(device_data)
        db.commit()
        return updated_device
 