from customtkinter import *
from PIL import Image
from tkinter import messagebox as mb
import mysql.connector
from dotenv import load_dotenv
import os
from modules import Modules

#.
class App:
    def __init__(self):
        self.app=CTk()
        self.app.title("App")
        self.center_window(self.app, 600, 680)
        self.app.resizable(False, False)
        
        #$########## COLORS ############
        self.primary_color = "#A9D9D9"
        self.secondary_color = "#5075BF"
        self.third_color = "#8BA5D9"
        self.fourth_color = "#1C418C"
        self.fifth_color = "#81A5A5"
        
        self.app.config(bg=self.fifth_color)

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
        
#
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
        self.center_window(modulos.root, 800, 740)
        self.conexion.close()
    
    
    #*################## WIDGETSS ######################
    def widgets(self):
        person_image = CTkImage(Image.open(os.path.join(self.carpeta_imagenes, "Persona.png")), size=(150, 200))

        frame_all = CTkFrame(
            self.app,
            fg_color=self.primary_color,
            corner_radius=30,
            bg_color=self.fifth_color
        )
        frame_all.pack(pady=30, padx=30, fill="both", expand=True)
        
        label_person_image= CTkLabel(
            frame_all,
            image=person_image,
            text="",
            fg_color=self.primary_color
        )
        label_person_image.pack(pady=30)
        
        label_person_text = CTkLabel(
            frame_all,
            text="Hola, ¿Cómo te llamas?\n¿Quiéres acompañarme?",
            font=("Arial", 35, "bold"),
            fg_color=self.primary_color,
            text_color=self.fourth_color
        )
        label_person_text.pack()
        
        self.user_entry = CTkEntry(
            frame_all,
            placeholder_text="    Me llamo...",
            placeholder_text_color="#DDDDDD",
            font=("Arial", 25),
            text_color="white",
            width=200,
            height=50,
            bg_color=self.primary_color,
            fg_color=self.secondary_color,
            border_color="white"
        )
        self.user_entry.pack(pady=(20,0))
        
        self.password_entry = CTkEntry(
            frame_all,
            placeholder_text="    Contraseña",
            placeholder_text_color="#DDDDDD",
            font=("Arial", 25),
            text_color="white",
            width=200,
            height=50,
            bg_color=self.primary_color,
            fg_color=self.secondary_color,
            border_color="white"
        )
        self.password_entry.pack(pady=(15,15))
        
        self.label_info = CTkLabel(
            frame_all,
            text="Ingresa tus credenciales...\nSi eres nuevo se creara una cuenta",
            font=("Arial", 10, "bold"),
            fg_color=self.primary_color,
            bg_color=self.primary_color,
            text_color="#000000"
        )
        self.label_info.pack(pady=(3,15))
        
        button = CTkButton(
            frame_all,
            text="Claro...",
            font=("Arial", 25),
            width=100,
            height=50,
            command=self.log_reg,
            bg_color=self.primary_color
        )
        button.pack()
        
    
    
if __name__ == "__main__":
    App()
    