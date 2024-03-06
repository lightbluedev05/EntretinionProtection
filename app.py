from customtkinter import *
from PIL import Image
from tkinter import messagebox as mb
import mysql.connector
from dotenv import load_dotenv
import os
from modules import Modules

class App:
    def __init__(self):
        self.app=CTk()
        self.app.title("App")
        self.center_window(self.app, 600, 580)
        self.app.resizable(False, False)
        
        #$####### RES ROUTE ############
        carpeta_principal = os.path.dirname(__file__)
        self.carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")
        
        #$####### MYSQL CONNECTION ############
        load_dotenv()
        host=os.getenv("HOST")
        user=os.getenv("USER")
        password=os.getenv("PASSWORD")
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        
        self.widgets()
        self.app.mainloop()
        

    #*############ FUNCTIONS ################
    def center_window(self, window, width , height):
        ancho_pantalla = window.winfo_screenwidth()
        alto_pantalla = window.winfo_screenheight()
        x = (ancho_pantalla - width) // 2
        y = (alto_pantalla - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def log_reg(self):
        cursor = self.conexion.cursor()
        
        self.username=self.user_entry.get().strip()
        password=self.password_entry.get().strip()
        
        cursor.execute(f"SELECT `username` FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
        ver_user = []
        for bd in cursor:
            ver_user.append(bd[0])

        if self.username in ver_user:
            cursor.execute(f"SELECT `password` FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
            ver_pass = []
            for bd in cursor:
                ver_pass.append(bd[0])
            
            if password in ver_pass:
                self.go_modules()
            else:
                mb.showerror("Error", "La contraseña es incorrecta")
        else:
            cursor.execute(f"INSERT INTO btibyrq3spz8nqhn2drh.users (`username`, `password`) VALUES ('{self.username}', '{password}')")
            self.conexion.commit()
            self.go_modules()
    
    def go_modules(self):
        self.app.withdraw()
        modulos = Modules(self.app, self.username)
        self.center_window(modulos.root, 800, 600)
    
    
    #*################## WIDGETSS ######################
    def widgets(self):
        person_image = CTkImage(Image.open(os.path.join(self.carpeta_imagenes, "Persona.png")), size=(150, 200))
    
        label_person_image= CTkLabel(
            self.app,
            image=person_image,
            text=""
        )
        label_person_image.pack(pady=30)
        
        label_person_text = CTkLabel(
            self.app,
            text="Hola, ¿Cómo te llamas?\n¿Quiéres acompañarme?",
            font=("Arial", 35)
        )
        label_person_text.pack()
        
        self.user_entry = CTkEntry(
            self.app,
            placeholder_text="    Me llamo...",
            font=("Arial", 25),
            text_color="white",
            width=200,
            height=50
        )
        self.user_entry.pack(pady=(20,0))
        
        self.password_entry = CTkEntry(
            self.app,
            placeholder_text="    Contraseña",
            font=("Arial", 25),
            text_color="white",
            width=200,
            height=50
        )
        self.password_entry.pack(pady=(15,30))
        
        button = CTkButton(
            self.app,
            text="Claro...",
            font=("Arial", 25),
            width=100,
            height=50,
            command=self.log_reg
        )
        button.pack()
    
    
if __name__ == "__main__":
    App()
    