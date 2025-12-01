from database.config import SessionLocal
from database.models.categoria_model import Categoria


class CategoriaRepository:
    @staticmethod
    def crear_categoria(datos):
        db = SessionLocal()
        categoria = Categoria(**datos)
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        db.close()
        return categoria

    @staticmethod
    def obtener_por_id(id_categoria):
        db = SessionLocal()
        categoria = db.query(Categoria).get(id_categoria)
        db.close()
        return categoria

    @staticmethod
    def obtener_todas():
        db = SessionLocal()
        categorias = db.query(Categoria).all()
        db.close()
        return categorias

    @staticmethod
    def eliminar_categoria(id_categoria):
        db = SessionLocal()
        categoria = db.query(Categoria).get(id_categoria)
        if categoria:
            db.delete(categoria)
            db.commit()
        db.close()
