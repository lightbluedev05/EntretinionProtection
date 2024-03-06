from customtkinter import *
from PIL import Image
from tkinter import messagebox
from seguridad import Seguridad

class App:
    def __init__(self):
        app=CTk()
        app.title("App")
        center_window(app, 600, 500)
        app.resizable(False, False)
        
        #$####### FRAME 1 ########

def center_window(ventana, ancho , alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    
def si():
    nombre = usuario_entry.get().strip()  # Obtener el nombre introducido por el usuario
    if nombre:
        messagebox.showinfo("ATENCIÓN CIUDADANO", "Mensaje...")
        ventana_centrar_registro = Seguridad(app)
        centrar(ventana_centrar_registro.seguridad, 800, 600)
        app.withdraw()
    else:
        messagebox.showerror("Error", "Por favor, introduzca un nombre.")

if __name__ == "__main__":
    app = CTk()
    app.title("App test")
    centrar(app, 600, 500)
    app.resizable(False, False)

    carpeta_principal = os.path.dirname(__file__)
    carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")
    
    ingreso_imagen_persona = CTkImage(Image.open(os.path.join(carpeta_imagenes, "Persona.png")), size=(150, 200))
    
    label_imagen_persona= CTkLabel(app, image=ingreso_imagen_persona, text="")
    label_imagen_persona.pack(pady=20)
    
    label_texto_persona = CTkLabel(app, text="Hola, ¿Cómo te llamas?\n¿Quiéres acompañarme?", font=("Arial", 35))
    label_texto_persona.pack()
    
    usuario_entry = CTkEntry(app, placeholder_text="    Me llamo...", font=("Arial", 25), text_color="white",
                            width=200, height=50)
    usuario_entry.pack(pady=20)
    
    boton_si = CTkButton(app, text="Si", font=("Arial", 25), width=100, height=50, command=si)
    boton_si.pack()
    
    app.mainloop()