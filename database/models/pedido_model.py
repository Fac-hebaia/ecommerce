from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    idPedido = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey("usuarios.idUsuario"), nullable=False)
    idFactura = Column(Integer, ForeignKey("facturas.idFactura"), nullable=False)
    
    estado = Column(Enum("Entregado","Pendiente","Cancelado","Enviado","Pagado","Reembolso"), nullable=True)
    fecha = Column(DateTime, nullable=False)

    usuario = relationship("Usuario")
    factura = relationship("Factura")
