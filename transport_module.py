from tkinter import messagebox
from customtkinter import *
from PIL import Image
import os

#.
class TransportModule:
    def __init__(self, ventana):
        self.ventana = ventana
        self.transport = CTkToplevel(self.ventana)
        self.transport.title("App")
        self.transport.config(bg="#bfd7ff")
        self.transport.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.transport.resizable(False, False)
        
        
        self.transport.geometry("880x600")
        
        
        self.primary_color = "#A9D9D9" #verde clarito
        self.secondary_color = "#5075BF" #azul medio
        self.third_color = "#8BA5D9" #azul bajo
        self.fourth_color = "#1C418C" #azul fuerte
        self.fifth_color = ""
        
        self.widgets()
        
    def cerrar_ventana(self):
        self.ventana.deiconify()
        self.transport.destroy()
    
    def mostrar_level_1(self):
        # Limpiar el frame derecho
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()
        
        frame1 = CTkFrame(self.frame_derecho, fg_color="#9bb1ff",
                        corner_radius=20,
                        border_width=5,
                        border_color="black",
                        )
        frame1.pack(padx=30, pady=15, fill="x")
        
        label_level = CTkLabel(frame1,
                            text="Quedaste con un amigo en su casa, pero se te pasó la hora y ya es de noche. Tienes algo urgente que hacer en tu casa, así que tienes que volver rápido. ¿Qué ruta tomarías para llevar a cabo esta tarea de la forma más segura posible?",
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 24),
                            wraplength=530,
                            justify="center",
                            )
        label_level.pack(padx=6, pady=6)
        
        frame2 = CTkFrame(self.frame_derecho, fg_color=self.primary_color)
        frame2.pack(fill="x")
        
        boton_a = CTkButton(frame2,
                            text="Tomaré un taxi\npara llegar a mi destino",
                            bg_color=self.primary_color,
                            text_color="white",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label("1"))
        boton_a.pack(side="left", padx=(15,0))
        
        boton_b = CTkButton(frame2,
                            text="Caminaré hasta la parada\nde buses más cercana",
                            bg_color=self.primary_color,
                            text_color="white",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label("2"))
        boton_b.pack(side="right", padx=15)
        
        frame3 = CTkFrame(self.frame_derecho, fg_color=self.primary_color)
        frame3.pack(fill="x", pady=30)

        boton_c = CTkButton(frame3,
                            text="Le pedire a mi amigo que\nme acompañe hasta un lugar\nseguro donde pueda tomar un\ncolectivo",
                            bg_color=self.primary_color,
                            text_color="white",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label("3"))
        boton_c.pack(side="left", padx=(15,0))

        boton_d = CTkButton(frame3,
                            text="Usaré una aplicación de\ntaxi para que me\nlleve hasta mi casa",
                            bg_color=self.primary_color,
                            text_color="white",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label("4"))
        boton_d.pack(side="right", padx=15)

        frame4 = CTkFrame(self.frame_derecho, fg_color=self.primary_color)
        frame4.pack(fill="x", side="bottom")

        self.label_texto = CTkLabel(frame4,
                                    text="",
                                    bg_color=self.primary_color,
                                    text_color="white",
                                    font=("Arial", 20),
                                    width=50)
        self.label_texto.pack(pady=30, padx=30)


    def actualizar_label(self, texto):
        self.label_texto.configure(text=texto)


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

        
        frame_derecho = CTkFrame(self.transport, width=640, fg_color=self.primary_color, corner_radius=0)
        frame_derecho.pack(side="right", fill="both", expand=True)
        frame_derecho.pack_propagate(False)
        
        
        self.frame_derecho = frame_derecho  # Guardar referencia al frame derecho
        
        frame_izquierdo = CTkFrame(self.transport, fg_color=self.third_color, corner_radius=0, width=240)
        frame_izquierdo.pack(side="left", fill="y")
        frame_izquierdo.pack_propagate(False)
        
        imagen_autobus = CTkImage(Image.open(os.path.join(carpeta_imagenes, "autobus.png")), size=(150, 130))
        label_autobus = CTkLabel(frame_izquierdo, image=imagen_autobus , text="", bg_color=self.third_color)
        label_autobus.pack(pady=(15,10), padx=5)
        
        
        # Crear botones Level del 1 al 6
        boton_level1 = CTkButton(frame_izquierdo,
                                text=" Level 1",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_1,
                                hover_color=self.fourth_color)
        boton_level1.pack(pady=10, fill="x")

        boton_level2 = CTkButton(frame_izquierdo,
                                text=" Level 2",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_2,
                                hover_color=self.fourth_color)
        boton_level2.pack(pady=10, fill="x")

        boton_level3 = CTkButton(frame_izquierdo,
                                text=" Level 3",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_3,
                                hover_color=self.fourth_color)
        boton_level3.pack(pady=10, fill="x")

        boton_level4 = CTkButton(frame_izquierdo,
                                text=" Level 4",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_4,
                                hover_color=self.fourth_color)
        boton_level4.pack(pady=10, fill="x")

        boton_level5 = CTkButton(frame_izquierdo,
                                text=" Level 5",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_5,
                                hover_color=self.fourth_color)
        boton_level5.pack(pady=10, fill="x")

        boton_level6 = CTkButton(frame_izquierdo,
                                text=" Level 6",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_6,
                                hover_color=self.fourth_color)
        boton_level6.pack(pady=10, fill="x")

        boton_atras = CTkButton(frame_izquierdo,
                                text=" SALIR",
                                anchor="center",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand1",
                                command=self.cerrar_ventana,
                                hover_color="#D94A4A")
        boton_atras.pack(pady=10, fill="x")
        
if __name__ == "__main__":
    root = CTk()
    
    username = "Miguel"
    
    trans = TransportModule(root)
    
    
    root.mainloop()