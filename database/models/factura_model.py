from sqlalchemy import Column, Integer, DateTime, Numeric
from database.config import Base

class Factura(Base):
    __tablename__ = "facturas"

    idFactura = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    montoTotal = Column(Numeric(15,2), nullable=False)
