from tkinter import messagebox
from customtkinter import *
from PIL import Image
import os

class TransportModule:
    def __init__(self, ventana):
        self.ventana = ventana
        self.transport = CTkToplevel(self.ventana)
        self.transport.title("App")
        self.transport.config(bg="#bfd7ff")
        self.transport.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.transport.resizable(False, False)
        
        self.widgets()
        
    def cerrar_ventana(self):
        self.ventana.deiconify()
        self.transport.destroy()
    
    def mostrar_level_1(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho,fg_color="#9bb1ff",
                        corner_radius=20)
        frame1.pack(padx=30, pady=30, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="¡LEVEL 1!",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 40, "bold"))
        label_level.pack(padx=10, pady=30)

    def mostrar_level_2(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho,fg_color="#9bb1ff",
                        corner_radius=20)
        frame1.pack(padx=30, pady=30, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="¡LEVEL 2!",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 40, "bold"))
        label_level.pack(padx=10, pady=30)

    # Repite el mismo patrón para los niveles restantes

    def mostrar_level_3(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho,fg_color="#9bb1ff",
                        corner_radius=20)
        frame1.pack(padx=30, pady=30, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="¡LEVEL 3!",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 40, "bold"))
        label_level.pack(padx=10, pady=30)

    def mostrar_level_4(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho,fg_color="#9bb1ff",
                        corner_radius=20)
        frame1.pack(padx=30, pady=30, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="¡LEVEL 4!",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 40, "bold"))
        label_level.pack(padx=10, pady=30)

    def mostrar_level_5(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho,fg_color="#9bb1ff",
                        corner_radius=20)
        frame1.pack(padx=30, pady=30, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="¡LEVEL 5!",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 40, "bold"))
        label_level.pack(padx=10, pady=30)

    def mostrar_level_6(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho,fg_color="#9bb1ff",
                        corner_radius=20)
        frame1.pack(padx=30, pady=30, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="¡LEVEL 6!",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 40, "bold"))
        label_level.pack(padx=10, pady=30)
    
    def widgets(self):
        
        carpeta_principal = os.path.dirname(__file__)
        carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")
        
        frame_derecho = CTkFrame(self.transport, width=640, fg_color="#bfd7ff", corner_radius=0)
        frame_derecho.pack(side="right", fill="both", expand=True)
        frame_derecho.pack_propagate(False)
        
        
        self.frame_derecho = frame_derecho  # Guardar referencia al frame derecho
        
        frame_izquierdo = CTkFrame(self.transport, fg_color="#9bb1ff", corner_radius=0, width=240)
        frame_izquierdo.pack(side="left", fill="y")
        frame_izquierdo.pack_propagate(False)
        
        
        # Crear botones Level del 1 al 6
        boton_level1 = CTkButton(frame_izquierdo,
                                text=" Level 1",
                                anchor="w",
                                fg_color="#9bb1ff",
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_1)
        boton_level1.pack(pady=10, fill="x")

        boton_level2 = CTkButton(frame_izquierdo,
                                text=" Level 2",
                                anchor="w",
                                fg_color="#9bb1ff",
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_2)
        boton_level2.pack(pady=10, fill="x")

        boton_level3 = CTkButton(frame_izquierdo,
                                text=" Level 3",
                                anchor="w",
                                fg_color="#9bb1ff",
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_3)
        boton_level3.pack(pady=10, fill="x")

        boton_level4 = CTkButton(frame_izquierdo,
                                text=" Level 4",
                                anchor="w",
                                fg_color="#9bb1ff",
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_4)
        boton_level4.pack(pady=10, fill="x")

        boton_level5 = CTkButton(frame_izquierdo,
                                text=" Level 5",
                                anchor="w",
                                fg_color="#9bb1ff",
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_5)
        boton_level5.pack(pady=10, fill="x")

        boton_level6 = CTkButton(frame_izquierdo,
                                text=" Level 6",
                                anchor="w",
                                fg_color="#9bb1ff",
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_6)
        boton_level6.pack(pady=10, fill="x")

        boton_atras = CTkButton(frame_izquierdo,
                                text=" SALIR",
                                anchor="center",
                                fg_color="#9bb1ff",
                                text_color="#EE7969",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand1",
                                command=self.cerrar_ventana)
        boton_atras.pack(pady=10, fill="x")