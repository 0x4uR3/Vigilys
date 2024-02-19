from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from backend.database import Base
    
class Devices(Base):
    __tablename__ = "devices"
    no_device = Column(Integer, primary_key=True, index=True, nullable=False)
    nwk_addr = Column(Integer, index=True, nullable=False)
    model_id = Column(String(35), nullable=False, index=True)
    ieee_addr = Column(String(25), nullable=False)
    location = Column(String(20), nullable=False, default="")
    alive = Column(Integer,nullable=False, default=0)
    no_parent = Column(Integer,nullable=False, default=0)
    device_type = Column(String(15), nullable=False, default="")
    report = Column(String(25), nullable=False, default="")
    reportbis = Column(String(25), nullable=False, default="")
    unit = Column(Integer,nullable=False, default=0)
    unitbis = Column(Integer,nullable=False, default=0)
    room = Column(String(50), nullable=False, default="")
    manuf_code = Column(Integer,nullable=False, default=-1)
    app_version = Column(Integer,nullable=False, default=0)
    residence = Column(String(35), nullable=False, default="")
    category = Column(Integer,nullable=False, default=0)
    stack_version = Column(Integer,nullable=False, default=0)
    last_report = Column(String(30), nullable=False, default="")
    hw_version = Column(Integer,nullable=False, default=0)
    zcl_version = Column(Integer,nullable=False, default=0)
    date_code = Column(String(12), nullable=False, default="")
    theme = Column(Integer,nullable=False, default=0)
    icone = Column(String(32), nullable=False, default="")
    zone_type = Column(Integer,nullable=False, default=-1)
    device_id = Column(Integer, nullable=False, default=65535)
    def __repr__(self):
        return 'Device(no_device=%s)' % (self.no_device)
