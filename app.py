from views.IniciarSesion import IniciarSesion
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from database.config import engine, Base

Base.metadata.create_all(bind=engine)

Inicio_sesion = IniciarSesion()
Inicio_sesion.mainloop()
