from tkinter import messagebox
from customtkinter import *
from PIL import Image
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="159789",
    database="login"
)

cursor = conexion.cursor()

class User:
    def __init__(self, username, contra):
        self.username = username
        self.contra = contra

    def guardar_en_bd(self):
        cursor.execute("INSERT INTO clientes (nombre, contra) VALUES (%s, %s)", (self.username, self.contra))
        conexion.commit()

    @staticmethod
    def cargar_de_bd(username):
        cursor.execute("SELECT nombre, contra FROM clientes WHERE nombre = %s", (username,))
        resultado = cursor.fetchone()
        if resultado:
            return User(resultado[0], resultado[1])
        else:
            return None

class Seguridad:

    def __init__(self, ventana):
        self.ventana = ventana
        self.seguridad = CTkToplevel(self.ventana)
        self.seguridad.title("App contra la inseguridad")
        self.seguridad.config(bg="#9bb1ff")
        self.seguridad.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.seguridad.resizable(False, False)
        
        self.widgets()

    def cerrar_ventana(self):
        self.ventana.destroy()


    def widgets(self):
        label_prueba = CTkLabel(self.seguridad, text="Prueba", font=("Arial", 25))