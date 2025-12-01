from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base

class DetallePedido(Base):
    __tablename__ = "detalles_pedido"

    idProducto = Column(Integer, ForeignKey("productos.idProducto"), primary_key=True)
    idPedido = Column(Integer, ForeignKey("pedidos.idPedido"), primary_key=True)
    
    precio = Column(Numeric(15,2), nullable=False)
    cantidad = Column(Integer, nullable=False)

    producto = relationship("Producto")
    pedido = relationship("Pedido")
