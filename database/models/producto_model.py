from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base

class Producto(Base):
    __tablename__ = "productos"

    idProducto = Column(Integer, primary_key=True)
    idCategoria = Column(Integer, ForeignKey("categorias.idCategoria"), nullable=False)
    idUsuario = Column(Integer, ForeignKey("usuarios.idUsuario"), nullable=False)
    
    stock = Column(Integer, nullable=False)
    fechaSubido = Column(Date, nullable=False)
    descripcion = Column(String(250), nullable=False)
    precio = Column(Numeric(15,2), nullable=False)

    categoria = relationship("Categoria")
    usuario = relationship("Usuario")
