from customtkinter import *
from dotenv import load_dotenv
import os
import mysql.connector
from add_reports import AddReport

class Reports:
    def __init__(self, master):
        self.app=CTkToplevel(master)
        self.app.title("App")
        self.center_window(self.app, 600, 740)
        self.app.resizable(False, False)
        self.app.grab_set()
        
        #$########## COLORS ############
        self.primary_color = "#A9D9D9"
        self.secondary_color = "#5075BF"
        self.third_color = "#8BA5D9"
        self.fourth_color = "#1C418C"
        self.fifth_color = "#81A5A5"
        
        self.app.config(bg=self.fifth_color)
        
        #$####### MYSQL CONNECTION ############
        self.host="btibyrq3spz8nqhn2drh-mysql.services.clever-cloud.com"
        self.user="uklu2xhrdmj6v1w9"
        self.password="n9N3OZ7LHYaH6D7VFYqZ"
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
        )
        
        self.widgets()
    
    
    #*############### FUNCTIONS ################
    def center_window(self, window, width , height):
        ancho_pantalla = window.winfo_screenwidth()
        alto_pantalla = window.winfo_screenheight()
        x = (ancho_pantalla - width) // 2
        y = (alto_pantalla - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def open_add_report(self):
        self.app.withdraw
        AddReport(self.app)
        
    
    def reload_reports(self):
        conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
        )
        
        for widget in self.frame_all.winfo_children():
            widget.destroy()
        
        cursor2 = conexion.cursor()
        cursor2.execute("SELECT * FROM btibyrq3spz8nqhn2drh.reports")
        
        reports=cursor2.fetchall()
        
        for new in reports:
            frame_new = CTkFrame(
                self.frame_all,
                fg_color=self.secondary_color,
                corner_radius=20,
                bg_color=self.primary_color,
                height=120
            )
            frame_new.pack(pady=(15,0), padx=15, fill="both")
            
            report_name = CTkLabel(
                frame_new,
                text=f"Reporte hecho por {new[1]}",
                font=("Roboto", 15, "bold"),
                text_color="white"
            )
            report_name.pack(pady=(5,0), padx=20)
            
            little_frame = CTkFrame(
                frame_new,
                fg_color=self.secondary_color,
                bg_color=self.secondary_color
            )
            little_frame.pack(pady=0, padx=20, fill="x")
            
            place_report = CTkLabel(
                little_frame,
                text=f"Lugar: {new[2]}",
                font=("Roboto", 12),
                text_color="white"
            )
            place_report.pack(pady=0, padx=20, side="left")
            
            date_report = CTkLabel(
                little_frame,
                text=f"Fecha: {new[3]}",
                font=("Roboto", 12),
                text_color="white"
            )
            date_report.pack(pady=0, padx=20, side="right")
            
            report_text = CTkLabel(
                frame_new,
                text=f"{new[4]}",
                font=("Roboto", 15),
                text_color="white",
                wraplength=450,
                justify="left"
            )
            report_text.pack(pady=(0,10))
        conexion.close()
        self.app.after(200, self.app.update_idletasks)
    
    
    #*################ WIDGETS ################
    def widgets(self):
        title_label = CTkLabel(
            self.app,
            text="REPORTES 24/7 [:)",
            font=("Arial", 50, "bold"),
            text_color="white",
            fg_color=self.fourth_color,
            bg_color=self.fifth_color,
            height=90,
            width=270,
            corner_radius=30,
        )
        title_label.pack(pady=(20,0), fill="x", padx=30)
        
        self.frame_all = CTkScrollableFrame(
            self.app,
            fg_color=self.primary_color,
            bg_color=self.fifth_color,
            corner_radius=30,
            border_width=5,
            border_color=self.fourth_color
        )
        self.frame_all.pack(pady=(20,15), padx=30, fill="both", expand=True)
        
        frame_buttons = CTkFrame(
            self.app,
            fg_color=self.fifth_color,
            bg_color=self.fifth_color,
        )
        frame_buttons.pack(pady=(20,15), padx=30, fill="x", expand=False)
        
        add_button = CTkButton(
            frame_buttons,
            fg_color=self.fourth_color,
            text_color="white",
            text="NUEVO REPORTE",
            font=("Arial", 20, "bold"),
            height=50,
            width=150,
            corner_radius=20,
            bg_color=self.fifth_color,
            border_color="white",
            border_width=2,
            command=self.open_add_report
        )
        add_button.pack(pady=(0,15), side = "left")
        
        reload_button = CTkButton(
            frame_buttons,
            fg_color=self.fourth_color,
            text_color="white",
            text="RECARGAR REPORTES",
            font=("Arial", 20, "bold"),
            height=50,
            width=150,
            corner_radius=20,
            bg_color=self.fifth_color,
            border_color="white",
            border_width=2,
            command=self.reload_reports
        )
        reload_button.pack(pady=(0,15), side= "right")
        
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM btibyrq3spz8nqhn2drh.reports")
        
        for new in cursor:
            frame_new = CTkFrame(
                self.frame_all,
                fg_color=self.secondary_color,
                corner_radius=20,
                bg_color=self.primary_color,
                height=120
            )
            frame_new.pack(pady=(15,0), padx=15, fill="both")
            
            report_name = CTkLabel(
                frame_new,
                text=f"Reporte hecho por {new[1]}",
                font=("Roboto", 15, "bold"),
                text_color="white"
            )
            report_name.pack(pady=(5,0), padx=20)
            
            little_frame = CTkFrame(
                frame_new,
                fg_color=self.secondary_color,
                bg_color=self.secondary_color
            )
            little_frame.pack(pady=0, padx=20, fill="x")
            
            place_report = CTkLabel(
                little_frame,
                text=f"Lugar: {new[2]}",
                font=("Roboto", 12),
                text_color="white"
            )
            place_report.pack(pady=0, padx=20, side="left")
            
            date_report = CTkLabel(
                little_frame,
                text=f"Fecha: {new[3]}",
                font=("Roboto", 12),
                text_color="white"
            )
            date_report.pack(pady=0, padx=20, side="right")
            
            report_text = CTkLabel(
                frame_new,
                text=f"{new[4]}",
                font=("Roboto", 15),
                text_color="white",
                wraplength=450,
                justify="left"
            )
            report_text.pack(pady=(0,10))
        self.conexion.close()



if __name__ == "__main__":
    root = CTk()
    Reports(root)
    root.mainloop()