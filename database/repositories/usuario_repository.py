from database.config import SessionLocal
from database.models.usuario_model import Usuario


class UsuarioRepository:
    @staticmethod
    def crear_usuario(datos):
        db = SessionLocal()
        usuario = Usuario(**datos)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        db.close()
        return usuario

    @staticmethod
    def iniciar_sesion(email, contrasenia):
        db = SessionLocal()
        usuario = (
            db.query(Usuario).filter_by(email=email, contrasenia=contrasenia).first()
        )
        db.close()
        return usuario.to_dict() if usuario else None

    @staticmethod
    def obtener_todos():
        db = SessionLocal()
        usuarios = db.query(Usuario).all()
        db.close()
        return usuarios

    @staticmethod
    def eliminar_usuario(id_usuario):
        db = SessionLocal()
        usuario = db.query(Usuario).get(id_usuario)
        if usuario:
            db.delete(usuario)
            db.commit()
        db.close()
