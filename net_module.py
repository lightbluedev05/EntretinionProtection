from tkinter import messagebox
from customtkinter import *
from PIL import Image
import os
import mysql.connector
from dotenv import load_dotenv

#.
class Netmodule:
    def __init__(self, ventana, username):
        self.ventana = ventana
        self.inter = CTkToplevel(self.ventana)
        self.inter.title("App")
        self.inter.config(bg="#bfd7ff")
        self.inter.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.inter.resizable(False, False)
        
        self.username = username
        
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
        
        self.inter.geometry("880x600")
        
        
        self.primary_color = "#A9D9D9" #verde clarito
        self.secondary_color = "#5075BF" #azul medio
        self.third_color = "#8BA5D9" #azul bajo
        self.fourth_color = "#1C418C" #azul fuerte
        self.fifth_color = ""
        
        # Inicialización de variables de nivel
        self.enunciado = ""
        self.opcion1 = ""
        self.opcion2 = ""
        self.opcion3 = ""
        self.opcion4 = ""
        self.nivel_actual = None
        
        self.get_points()
        
        self.widgets()
        

    def cerrar_ventana(self):
        self.inter.destroy()
        self.ventana.deiconify()

    def get_points(self):
        #$####### MYSQL CONNECTION ############
        load_dotenv()
        self.host=os.getenv("HOST")
        self.user=os.getenv("USER")
        self.password=os.getenv("PASSWORD")
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
        )
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"SELECT `module4` FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
        ver_points=[]
        for bd in self.cursor:
            ver_points.append(bd[0])
        self.points=ver_points[0]
        print(self.points)
    
#*#-----------------------------------------------------------------------------------------------------------------------

    def mostrar_level(self, enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, a, b, c):
        # Asignar valores para el nivel 1
        self.enunciado = enunciado
        self.opcion1 = opcion1
        self.consejo1 = consejo1
        self.opcion2 = opcion2
        self.consejo2 = consejo2
        self.opcion3 = opcion3
        self.consejo3 = consejo3
        self.nivel_actual = nivel_actual
        self.a = a
        self.b = b
        self.c = c
        
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
                            text=self.enunciado,
                            bg_color="#9bb1ff",
                            text_color="white",
                            font=("Arial", 19),
                            wraplength=530,
                            justify="center",
                            )
        label_level.pack(padx=6, pady=6)
        
        frame2 = CTkFrame(self.frame_derecho, fg_color=self.primary_color)
        frame2.pack(fill="x")
        
        self.boton_a = CTkButton(frame2,
                            text=self.opcion1,
                            bg_color=self.primary_color,
                            fg_color=self.primary_color,
                            text_color="black",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label(self.consejo1, a, b , c),
                            border_color="white",
                            border_width=3,
                            hover_color="#B8F25D")
        self.boton_a.pack(side="left", padx=(15,0))
        
        self.boton_b = CTkButton(frame2,
                            text=self.opcion2,
                            bg_color=self.primary_color,
                            fg_color=self.primary_color,
                            text_color="black",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label(self.consejo2, a, b, c),
                            border_color="white",
                            border_width=3,
                            hover_color="#B8F25D")
        self.boton_b.pack(side="right", padx=15)
        
        frame3 = CTkFrame(self.frame_derecho, fg_color=self.primary_color)
        frame3.pack(fill="x", pady=30)

        self.boton_c = CTkButton(frame3,
                            text=self.opcion3,
                            bg_color=self.primary_color,
                            fg_color=self.primary_color,
                            text_color="black",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label(self.consejo3, a, b, c),
                            border_color="white",
                            border_width=3,
                            hover_color="#B8F25D")
        self.boton_c.pack(padx=15)

        frame4 = CTkFrame(self.frame_derecho, fg_color=self.primary_color)
        frame4.pack(fill="x", side="bottom")

        self.label_texto = CTkLabel(frame4,
                                    text="",
                                    bg_color=self.primary_color,
                                    text_color="white",
                                    font=("Arial", 20),
                                    height=100)
        self.label_texto.pack(fill="x", side="bottom")

    def actualizar_label(self, texto, *botones):
        
        colores = {0: "#7CB679", 1: "#CCD06F", 2: "#D0726F"}

        for i, boton in enumerate(botones, start=1):
            color = colores.get(boton, "#7CB679")
            
            getattr(self, f"boton_{chr(96 + i)}").configure(
                fg_color=color, hover_color=color, command=None
            )

        self.label_texto.configure(text=texto)
        
        
        if self.points < self.nivel_actual:
            
            cursor = self.conexion.cursor()
            
            cursor.execute(f"UPDATE `btibyrq3spz8nqhn2drh`.`users` SET `module4` = '{self.nivel_actual}' WHERE (`username` = '{self.username}');")
            self.conexion.commit()
            
        if self.points < 6:
            if self.nivel_actual == 6:
                messagebox.showinfo("¡Felicidades!", "Haz completado el módulo.")
            
            if self.nivel_actual == 1:
                self.boton_level1.configure(state="disabled", text=" Level 1")
                self.boton_level2.configure(state="enabled", cursor="hand2", hover_color=self.fourth_color)
            elif self.nivel_actual == 2:
                self.boton_level2.configure(state="disabled", text=" Level 2")
                self.boton_level3.configure(state="enabled", cursor="hand2", hover_color=self.fourth_color)
            elif self.nivel_actual == 3:
                self.boton_level3.configure(state="disabled", text=" Level 3")
                self.boton_level4.configure(state="enabled", cursor="hand2", hover_color=self.fourth_color)
            elif self.nivel_actual == 4:
                self.boton_level4.configure(state="disabled", text=" Level 4")
                self.boton_level5.configure(state="enabled", cursor="hand2", hover_color=self.fourth_color)
            elif self.nivel_actual == 5:
                self.boton_level5.configure(state="disabled", text=" Level 5")
                self.boton_level6.configure(state="enabled", cursor="hand2", hover_color=self.fourth_color)
            elif self.nivel_actual == 6:
                self.boton_level6.configure(state="disabled", text=" Level 6")
                self.ventana.deiconify()
                self.inter.destroy()

#*#-----------------------------------------------------------------------------------------------------------------------
    def mostrar_level_1(self):
        enunciado = "Imagina que estás revisando tu cuenta bancaria en línea y descubres que ha habido una serie de transacciones no autorizadas. Al investigar más a fondo, te das cuenta de que tu información personal, como tu número de tarjeta de crédito y tu contraseña, ha sido comprometida y utilizada para realizar compras fraudulentas en varios sitios web."
        opcion1 = "Compartir tu información\npersonal y financiera en un\nsitio web no seguro que has\nencontrado en línea"
        consejo1 = "1"
        opcion2 = "Contactar inmediatamente a tu\nbanco para informarles sobre las\ntransacciones no autorizadas y\ncambiar tus contraseñas en todos\ntus cuentas en línea."
        consejo2 = "2"
        opcion3 = "Informar a las autoridades competentes\nsobre el robo de información y presentar\nun informe policial, además de contactar\na las agencias de crédito para\ncongelar tus informes de crédito."
        consejo3 = "3"
        nivel_actual = 1
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 2, 1, 0)
        
    def mostrar_level_2(self):
        enunciado = "Supongamos que has estado utilizando una red social popular y de repente comienzas a recibir mensajes insultantes y amenazantes de un usuario desconocido. A medida que pasan los días, el acoso se intensifica, con el usuario desconocido difundiendo rumores falsos sobre ti y publicando comentarios despectivos en tus publicaciones."
        opcion1 = "Responder a los mensajes y\nconfrontar al acosador\npúblicamente en la plataforma\nde redes sociales"
        consejo1 = "1"
        opcion2 = "Ignorar los mensajes y eliminar\nlas publicaciones ofensivas del\nacosador sin informar a\nnadie más sobre lo que\nestá sucediendo.."
        consejo2 = "1"
        opcion3 = "Bloquear al acosador, mantener evidencia\nde los mensajes y reportar el acoso a la\nplataforma de redes sociales y, si\nes necesario, a las autoridades."
        consejo3 = "1"
        nivel_actual = 2
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 2, 1, 0)

    def mostrar_level_3(self):
        enunciado = "Digamos que estás navegando por Internet en tu computadora portátil y de repente notas un rendimiento más lento y extraño en el sistema. Después de realizar un escaneo antivirus, descubres que tu dispositivo ha sido infectado por un malware sofisticado que ha comprometido tus datos personales y financiados y ahora tus archivos importantes están cifrados y no puedes acceder a ellos."
        opcion1 = " Ignorar la infección por\nmalware y continuar usando\ntu dispositivo normalmente.."
        consejo1 = "1"
        opcion2 = "Descargar software de eliminación\nde malware de un sitio web\nno verificado en un intento\nde eliminar el virus."
        consejo2 = "1"
        opcion3 = "Utilizar un software antivirus confiable\npara escanear y eliminar el malware, además de\nactualizar tus sistemas operativos y software\nregularmente para mantener la seguridad\nde tus dispositivos."
        consejo3 = "1"
        nivel_actual = 3
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 2, 1, 0)

    def mostrar_level_4(self):
        enunciado = "Imagina que descubres que alguien ha creado perfiles de redes sociales falsos utilizando tu nombre e información personal. Estos perfiles están siendo utilizados para difundir información falsa o inapropiada, lo que podría dañar tu reputación en línea."
        opcion1 = " Publicar mensajes agresivos o confrontacionales en\nrespuesta a los perfiles\nfalsos."
        consejo1 = "1"
        opcion2 = "Informar a la plataforma de redes\nsociales sobre los perfiles falsos\ny solicitar su eliminación."
        consejo2 = "1"
        opcion3 = "Cambiar tu configuración de\nprivacidad y ajustarla para limitar\nquién puede ver tu información\npersonal y publicaciones."
        consejo3 = "1"
        nivel_actual = 4
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 0, 1, 2)

    def mostrar_level_5(self):
        enunciado = "Estás trabajando en tu computadora de trabajo cuando de repente aparece un mensaje en pantalla informándote de que tus archivos han sido cifrados y que debes pagar un rescate en criptomonedas para recuperar el acceso a ellos. Tu empresa se enfrenta a una grave amenaza de ransomware que pone en peligro la seguridad de sus datos."
        opcion1 = "Pagar el rescate exigido por\nlos hackers para recuperar\nlos archivos cifrados."
        consejo1 = "1"
        opcion2 = "Apagar la computadora y no\ninformar a nadie sobre el\nataque de ransomware."
        consejo2 = "1"
        opcion3 = "Informar inmediatamente al departamento de\nTI de tu empresa sobre el ataque de ransomware\ny seguir sus instrucciones para mitigar el\ndaño y proteger los datos de la empresa."
        consejo3 = "1"
        nivel_actual = 5
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 2, 1, 0)

    def mostrar_level_6(self):  
        enunciado = "Recibes un mensaje directo en una red social de alguien que afirma ser un amigo tuyo y te pide que hagas clic en un enlace adjunto para ver una foto divertida. Sin embargo, al hacer clic en el enlace, descargas inadvertidamente malware en tu dispositivo, comprometiendo tu seguridad en línea."
        opcion1 = "Compartir el enlace malicioso con\ntus amigos para que también\npuedan ver la foto divertida"
        consejo1 = "1"
        opcion2 = "Hacer clic en el enlace y\nproporcionar información adicional\nsolicitada por el remitente."
        consejo2 = "1"
        opcion3 = " Ignorar el mensaje y no hacer\nclic en el enlace, y luego informar a la\nred social sobre el intento de phishing\npara que puedan tomar\nmedidas preventivas. "
        consejo3 = "1"
        nivel_actual = 6
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 2, 1, 0)

        
    def widgets(self):
        
        carpeta_principal = os.path.dirname(__file__)
        carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")

        
        frame_derecho = CTkFrame(self.inter, width=640, fg_color=self.primary_color, corner_radius=0)
        frame_derecho.pack(side="right", fill="both", expand=True)
        frame_derecho.pack_propagate(False)
        
        
        self.frame_derecho = frame_derecho  # Guardar referencia al frame derecho
        
        frame_izquierdo = CTkFrame(self.inter, fg_color=self.third_color, corner_radius=0, width=240)
        frame_izquierdo.pack(side="left", fill="y")
        frame_izquierdo.pack_propagate(False)
        
        imagen_autobus = CTkImage(Image.open(os.path.join(carpeta_imagenes, "digital.png")), size=(150, 130))
        label_autobus = CTkLabel(frame_izquierdo, image=imagen_autobus , text="", bg_color=self.third_color)
        label_autobus.pack(pady=(15,10), padx=5)
        
        
        # Crear botones Level del 1 al 6
        self.boton_level1 = CTkButton(frame_izquierdo,
                                text=" Level 1",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_1,
                                hover_color=self.fourth_color)
        self.boton_level1.pack(pady=10, fill="x")
        
        self.boton_level2 = CTkButton(frame_izquierdo,
                                text=" Level 2",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_2,
                                hover_color=self.fourth_color)
        self.boton_level2.pack(pady=10, fill="x")

        self.boton_level3 = CTkButton(frame_izquierdo,
                                text=" Level 3",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_3,
                                hover_color=self.fourth_color)
        self.boton_level3.pack(pady=10, fill="x")

        self.boton_level4 = CTkButton(frame_izquierdo,
                                text=" Level 4",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_4,
                                hover_color=self.fourth_color)
        self.boton_level4.pack(pady=10, fill="x")

        self.boton_level5 = CTkButton(frame_izquierdo,
                                text=" Level 5",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_5,
                                hover_color=self.fourth_color)
        self.boton_level5.pack(pady=10, fill="x")

        self.boton_level6 = CTkButton(frame_izquierdo,
                                text=" Level 6",
                                anchor="w",
                                fg_color=self.third_color,
                                text_color="white",
                                font=("Verdana", 30, "bold"),
                                corner_radius=0,
                                cursor="hand2",
                                command=self.mostrar_level_6,
                                hover_color=self.fourth_color)
        self.boton_level6.pack(pady=10, fill="x")

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
        
        if self.points ==0:
            self.boton_level2.configure(state="disabled")
            self.boton_level3.configure(state="disabled")
            self.boton_level4.configure(state="disabled")
            self.boton_level5.configure(state="disabled")
            self.boton_level6.configure(state="disabled")
        elif self.points == 1:
            self.boton_level1.configure(state="disabled")
            self.boton_level3.configure(state="disabled")
            self.boton_level4.configure(state="disabled")
            self.boton_level5.configure(state="disabled")
            self.boton_level6.configure(state="disabled")
        elif self.points == 2:
            self.boton_level1.configure(state="disabled")
            self.boton_level2.configure(state="disabled")
            self.boton_level4.configure(state="disabled")
            self.boton_level5.configure(state="disabled")
            self.boton_level6.configure(state="disabled")
        elif self.points == 3:
            self.boton_level1.configure(state="disabled")
            self.boton_level2.configure(state="disabled")
            self.boton_level3.configure(state="disabled")
            self.boton_level5.configure(state="disabled")
            self.boton_level6.configure(state="disabled")
        elif self.points == 4:
            self.boton_level1.configure(state="disabled")
            self.boton_level2.configure(state="disabled")
            self.boton_level3.configure(state="disabled")
            self.boton_level4.configure(state="disabled")
            self.boton_level6.configure(state="disabled")
        elif self.points == 5:
            self.boton_level1.configure(state="disabled")
            self.boton_level2.configure(state="disabled")
            self.boton_level3.configure(state="disabled")
            self.boton_level4.configure(state="disabled")
            self.boton_level5.configure(state="disabled")
        elif self.points == 6:
            self.boton_level1.configure(state="enabled", cursor="hand2")
            self.boton_level2.configure(state="enabled", cursor="hand2")
            self.boton_level3.configure(state="enabled", cursor="hand2")
            self.boton_level4.configure(state="enabled", cursor="hand2")
            self.boton_level5.configure(state="enabled", cursor="hand2")
            self.boton_level6.configure(state="enabled", cursor="hand2")
            
        print(self.points)
            



if __name__ == "__main__":
    root = CTk()
    
    username = "Pepito"
    
    trans = Netmodule(root)
    
    
    root.mainloop()