from customtkinter import *
import mysql.connector
from tkinter import messagebox
from transport_module import TransportModule
from event_module import Eventmodule
from calle_module import CalleModule
from net_module import Netmodule
from PIL import Image
import os
from dotenv import load_dotenv

class Modules:
    def __init__(self, master, username):
        #$######## PANTALLA ############
        self.master = master
        self.root = CTkToplevel(self.master)
        self.root.title("Modelos")
        self.root.grab_set()
        self.root.minsize(800, 770)
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        #$########## COLORS ############
        self.primary_color = "#A9D9D9"
        self.secondary_color = "#5075BF"
        self.third_color = "#8BA5D9"
        self.fourth_color = "#1C418C"
        self.fifth_color = ""

        self.root.config(bg=self.primary_color)

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
        
        self.username = username
        
        #*########### RES ##################
        carpeta_principal = os.path.dirname(__file__)
        self.carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")
        
        self.widgets()
        
    
    #.
    #*############### FUNCTIONS ################
    
    def cerrar_ventana(self):
        if messagebox.askokcancel("Salir", "¿Deseas salir del programa?"):
            self.master.destroy()

    def get_points(self):
        cursor=self.conexion.cursor()
        cursor.execute(f"SELECT * FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
        
        data=[]
        for bd in cursor:
            data.append(bd)

        p_1=data[0][2]
        p_2=data[0][3]
        p_3=data[0][4]
        p_4=data[0][5]
        
        suma = int((p_1 + p_2 + p_3 + p_4)/3)
        
        return suma
    
    
    def update_progress(self):
        for i in range (self.get_points()):
            self.progress_bar.step()
    
    
    def center_window(self, window, width , height):
        ancho_pantalla = window.winfo_screenwidth()
        alto_pantalla = window.winfo_screenheight()
        x = (ancho_pantalla - width) // 2
        y = (alto_pantalla - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def go_transport(self):
        self.root.withdraw()
        transporte = TransportModule(self.root, self.username)
        self.center_window(transporte.transport, 880, 600)
    
    def go_event(self):
        self.root.withdraw()
        evento = Eventmodule(self.root, self.username)
        self.center_window(evento.event, 880, 600)

    def go_calle(self):
        self.root.withdraw()
        calle = CalleModule(self.root, self.username)
        self.center_window(calle.call, 880, 600)
        
    def go_net(self):
        self.root.withdraw()
        inter = Netmodule(self.root, self.username)
        self.center_window(inter.inter, 880, 600)


    #*################ WIDGETS ################
    def widgets(self):
        autobus_image = CTkImage(Image.open(os.path.join(self.carpeta_imagenes, "autobus.png")), size=(150, 150))
        calendario_image = CTkImage(Image.open(os.path.join(self.carpeta_imagenes, "calendario.png")), size=(150, 150))
        parque_image = CTkImage(Image.open(os.path.join(self.carpeta_imagenes, "parque.png")), size=(150, 150))
        digital_image =CTkImage(Image.open(os.path.join(self.carpeta_imagenes, "digital.png")), size=(150, 150))
        
        title_label = CTkLabel(
            self.root,
            text=f"Hola {self.username}, completa los módulos de\naprendizaje ante situaciones de peligro :)",
            font=("Arial", 30, "bold"),
            fg_color=self.secondary_color,
            bg_color=self.primary_color,
            width=680,
            height=100,
            text_color="white",
            corner_radius=40
        )
        title_label.pack(pady=(30,20))
        
        #$############# FRAME 1 ##################
        frame_1 = CTkFrame(
            self.root,
            fg_color=self.primary_color,
            bg_color=self.primary_color,
        )
        frame_1.pack(fill = 'x', pady=(10,0), expand=True)
        
        
        module_1 = CTkButton(
            frame_1,
            corner_radius=10,
            bg_color=self.primary_color,
            fg_color=self.third_color,
            hover_color=self.fourth_color,
            text="  En el\n  transporte\n  público",
            font=("Arial", 27, "bold"),
            width=340,
            height=200,
            command=self.go_transport,
            image=autobus_image,
            compound="left",
            anchor="w"
        )
        module_1.pack(pady=15, side="left", padx=30)
        
        module_2 = CTkButton(
            frame_1,
            corner_radius=10,
            bg_color=self.primary_color,
            fg_color=self.third_color,
            hover_color=self.fourth_color,
            text="En algun\nevento\n o fiesta",
            font=("Arial", 27, "bold"),
            width=340,
            height=200,
            image=calendario_image,
            command=self.go_event,
        )
        module_2.pack(pady=15, side="right", padx=30)
        
        #$############# FRAME 2 ################
        frame_2 = CTkFrame(
            self.root,
            fg_color=self.primary_color,
            bg_color=self.primary_color,
        )
        frame_2.pack(fill = 'x', pady=(0,15), expand=True)
        
        module_3 = CTkButton(
            frame_2,
            corner_radius=10,
            bg_color=self.primary_color,
            fg_color=self.third_color,
            hover_color=self.fourth_color,
            text="En las\ncalles de\nla ciudad",
            font=("Arial", 27, "bold"),
            width=340,
            height=200,
            image=parque_image,
            command=self.go_calle,
        )
        module_3.pack(pady=15, side="left", padx=30)
        
        module_4 = CTkButton(
            frame_2,
            corner_radius=10,
            bg_color=self.primary_color,
            fg_color=self.third_color,
            hover_color=self.fourth_color,
            text="Con las\nnuevas\ntecnologias",
            font=("Arial", 27, "bold"),
            width=340,
            height=200,
            image=digital_image,
            command=self.go_net,
        )
        module_4.pack(pady=(15,5), side="right", padx=30)
        
        #$############### PROGRESS BAR ############
        title_bar = CTkLabel(
            self.root,
            text="Tu progreso <3",
            font=("Arial", 20, "bold"),
            fg_color=self.primary_color,
            text_color="white",
            bg_color=self.primary_color,
        )
        title_bar.pack(pady=(20,10))
        
        progress_frame = CTkFrame(
            self.root,
            fg_color=self.primary_color,
            bg_color=self.primary_color
        )
        progress_frame.pack(pady=(0,20))
        
        self.progress_bar = CTkProgressBar(
            progress_frame,
            progress_color=self.secondary_color,
            border_color=self.primary_color,
            corner_radius=50,
            height=20,
            width=400,
            bg_color=self.primary_color,
            fg_color="#FFFFFF",
            determinate_speed=6.25,
        )
        self.progress_bar.pack(pady=(0,20), side="left")
        self.progress_bar.set(0)
        
        refresh_button = CTkButton(
            progress_frame,
            text="Actualizar",
            font=("Arial", 20, "bold"),
            fg_color=self.primary_color,
            bg_color=self.primary_color,
            text_color="white",
            command=self.update_progress,
        )
        refresh_button.pack(side="right")
        
        for i in range (self.get_points()):
            self.progress_bar.step()
            
"""if __name__ == "__main__":
    root=CTk()
    username="Miguel"
    Modules(root, username)
    root.mainloop()"""