from database.config import SessionLocal
from database.models.pedido_model import Pedido


class PedidoRepository:
    @staticmethod
    def crear_pedido(datos):
        db = SessionLocal()
        pedido = Pedido(**datos)
        db.add(pedido)
        db.commit()
        db.refresh(pedido)
        db.close()
        return pedido

    @staticmethod
    def obtener_por_id(id_pedido):
        db = SessionLocal()
        pedido = db.query(Pedido).get(id_pedido)
        db.close()
        return pedido

    @staticmethod
    def obtener_todos(**filtros):
        db = SessionLocal()
        pedidos = (
            db.query(Pedido)
            .filter_by(**filtros)
            .join(Pedido.factura, Pedido.usuario)
            .all()
        )
        db.close()
        return pedidos

    @staticmethod
    def eliminar_pedido(id_pedido):
        db = SessionLocal()
        pedido = db.query(Pedido).get(id_pedido)
        if pedido:
            db.delete(pedido)
            db.commit()
        db.close()
