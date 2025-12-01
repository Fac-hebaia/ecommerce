from database.config import SessionLocal
from database.models.detalle_pedido_model import DetallePedido


class DetallePedidoRepository:
    @staticmethod
    def crear_detalle_pedido(datos):
        db = SessionLocal()
        detalle = DetallePedido(**datos)
        db.add(detalle)
        db.commit()
        db.refresh(detalle)
        db.close()
        return detalle

    @staticmethod
    def obtener_por_id(id_detalle):
        db = SessionLocal()
        detalle = db.query(DetallePedido).join(DetallePedido.producto).get(id_detalle)
        db.close()
        return detalle

    @staticmethod
    def obtener_todos(**filtros):
        db = SessionLocal()
        detalles = (
            db.query(DetallePedido)
            .filter_by(**filtros)
            .join(DetallePedido.producto)
            .all()
        )
        db.close()
        return detalles

    @staticmethod
    def eliminar_detalle_pedido(id_detalle):
        db = SessionLocal()
        detalle = db.query(DetallePedido).get(id_detalle)
        if detalle:
            db.delete(detalle)
            db.commit()
        db.close()
