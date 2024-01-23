from typing import List, Optional
from pydantic import BaseModel

class DeviceBase(BaseModel):
    no_device: int
    nwk_addr: int
    model_id: str
    ieee_addr: str
    location: str
    alive: int
    no_parent: int
    device_type: str
    report: str
    reportbis: str
    unit: int
    unitbis: int
    room: str
    manuf_code: int
    app_version: int
    residence: str
    category: int
    stack_version: int
    last_report: str
    hw_version: int
    zcl_version: int
    date_code: str
    theme: int
    icone: str
    zone_type: int
    device_id: int

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    class Config:
        from_attributes = True
