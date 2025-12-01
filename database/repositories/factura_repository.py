from database.config import SessionLocal
from database.models.factura_model import Factura


class FacturaRepository:
    @staticmethod
    def crear_factura(datos):
        db = SessionLocal()
        factura = Factura(**datos)
        db.add(factura)
        db.commit()
        db.refresh(factura)
        db.close()
        return factura

    @staticmethod
    def obtener_por_id(id_factura):
        db = SessionLocal()
        factura = db.query(Factura).get(id_factura)
        db.close()
        return factura

    @staticmethod
    def obtener_todas():
        db = SessionLocal()
        facturas = db.query(Factura).all()
        db.close()
        return facturas

    @staticmethod
    def eliminar_factura(id_factura):
        db = SessionLocal()
        factura = db.query(Factura).get(id_factura)
        if factura:
            db.delete(factura)
            db.commit()
        db.close()
