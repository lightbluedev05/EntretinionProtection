from customtkinter import *
from dotenv import load_dotenv
import os
from tkinter import messagebox as mb
import mysql.connector

class AddReport:
    def __init__(self, master):
        self.root = CTkToplevel(master)
        self.root.title("App")
        self.center_window(self.root, 450, 700)
        self.root.resizable(False, False)
        self.root.grab_set()
        
        #$########## COLORS ############
        self.primary_color = "#A9D9D9"
        self.secondary_color = "#5075BF"
        self.third_color = "#8BA5D9"
        self.fourth_color = "#1C418C"
        self.fifth_color = "#81A5A5"
        
        self.root.config(bg=self.fifth_color)
        
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
    
    
    #*############### FUNCTIONS ################
    def center_window(self, window, width , height):
        ancho_pantalla = window.winfo_screenwidth()
        alto_pantalla = window.winfo_screenheight()
        x = (ancho_pantalla - width) // 2
        y = (alto_pantalla - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def add_report(self):
        name = self.name_entry.get().strip()
        place = self.place_entry.get().strip()
        date = self.date_entry.get().strip()
        report = self.report_entry.get("1.0", "end-1c").strip()
        
        if name == "" or place == "" or date == "" or report == "":
            mb.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"INSERT INTO btibyrq3spz8nqhn2drh.reports (`reporter`, `place`, `date`, `report`) VALUES ('{name}', '{place}', '{date}', '{report}')")
            self.conexion.commit()
            mb.showinfo("Exito", "Reporte registrado con exito")
            self.root.destroy()
        except:
            mb.showerror("Error", "No se ha podido registrar el reporte en la red")    
            
    
    
    
    #*################# WIDGETS ################
    def widgets(self):
        
        frame_all = CTkFrame(
            self.root,
            fg_color=self.primary_color,
            bg_color=self.fifth_color,
            corner_radius=30,
            border_width=5,
            border_color=self.fourth_color
        )
        frame_all.pack(pady=(20,15), padx=30, fill="both", expand=True)
        
        name_label = CTkLabel(
            frame_all,
            text="Nombre o nombre clave:",
            font=("Arial", 20, "bold"),
            text_color=self.fourth_color,
            fg_color=self.primary_color,
            height=50,
            width=300,
        )
        name_label.pack(pady=(10,0), padx=5)
        
        self.name_entry =CTkEntry(
            frame_all,
            font=("Arial", 20),
            width=300,
            height=40,
            fg_color="white",
            text_color=self.fourth_color
        )
        self.name_entry.pack(pady=0, padx=5)
        
        place_label = CTkLabel(
            frame_all,
            text="Lugar del reporte:",
            font=("Arial", 20, "bold"),
            text_color=self.fourth_color,
            fg_color=self.primary_color,
            height=50,
            width=300,
        )
        place_label.pack(pady=(5,0), padx=5)
        
        self.place_entry =CTkEntry(
            frame_all,
            font=("Arial", 20),
            width=300,
            height=40,
            fg_color="white",
            text_color=self.fourth_color
        )
        self.place_entry.pack(pady=0, padx=5)
        
        date_label = CTkLabel(
            frame_all,
            text="Fecha (DD/MM/YYYY):",
            font=("Arial", 20, "bold"),
            text_color=self.fourth_color,
            fg_color=self.primary_color,
            height=50,
            width=300,
        )
        date_label.pack(pady=(5,0), padx=5)
        
        self.date_entry =CTkEntry(
            frame_all,
            font=("Arial", 20),
            width=300,
            height=40,
            fg_color="white",
            text_color=self.fourth_color
        )
        self.date_entry.pack(pady=0, padx=5)
        
        report_label = CTkLabel(
            frame_all,
            text="¿Que ha sucedido?",
            font=("Arial", 20, "bold"),
            text_color=self.fourth_color,
            fg_color=self.primary_color,
            height=50,
            width=300,
        )
        report_label.pack(pady=(5,0), padx=5)
        
        self.report_entry = CTkTextbox(
            frame_all,
            font=("Arial", 20),
            width=300,
            height=200,
            fg_color="white",
            text_color=self.fourth_color
        )
        self.report_entry.pack(pady=5, padx=5)
        
        add_report_button = CTkButton(
            frame_all,
            fg_color=self.fourth_color,
            text_color="white",
            text="AGREGAR REPORTE",
            font=("Arial", 20, "bold"),
            height=50,
            width=300,
            corner_radius=20,
            bg_color=self.primary_color,
            border_color="white",
            border_width=2,
            command=self.add_report
        )
        add_report_button.pack(pady=(20,0), padx=5)
