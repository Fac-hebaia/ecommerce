from database.config import SessionLocal
from database.models.producto_model import Producto


class ProductoRepository:
    @staticmethod
    def crear_producto(datos):
        db = SessionLocal()
        producto = Producto(**datos)
        db.add(producto)
        db.commit()
        db.refresh(producto)
        db.close()
        return producto

    @staticmethod
    def obtener_por_id(id_producto):
        db = SessionLocal()
        producto = db.query(Producto).join(Producto.categoria).get(id_producto)
        db.close()
        return producto

    @staticmethod
    def obtener_todos(**filtros):
        db = SessionLocal()
        productos = (
            db.query(Producto).filter_by(**filtros).join(Producto.categoria).all()
        )
        db.close()
        return productos

    @staticmethod
    def eliminar_producto(id_producto):
        db = SessionLocal()
        producto = db.query(Producto).get(id_producto)
        if producto:
            db.delete(producto)
            db.commit()
        db.close()
