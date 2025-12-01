from sqlalchemy import Column, Integer, String
from database.config import Base


class Categoria(Base):
    __tablename__ = "categorias"

    idCategoria = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
