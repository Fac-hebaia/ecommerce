from sqlalchemy import Column, Integer, String
from database.config import Base
from database.models.base_mixin import SerializerMixin

class Usuario(Base, SerializerMixin):
    __tablename__ = "usuarios"

    idUsuario = Column(Integer, primary_key=True)
    dni = Column(String(20), nullable=False)
    telefono = Column(String(30), nullable=False)
    contrasenia = Column(String(18), nullable=False)
    email = Column(String(30), nullable=False)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    direccion = Column(String(50), nullable=False)
    pais = Column(String(30), nullable=False)
    provincia = Column(String(20), nullable=False)
    codigoPostal = Column(String(10), nullable=False)
    ciudad = Column(String(30))
    calle = Column(String(30))
    numeracion = Column(String(30))
