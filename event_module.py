from tkinter import messagebox
from customtkinter import *
from PIL import Image
import os
import mysql.connector
from dotenv import load_dotenv

#..
class Eventmodule:
    def __init__(self, ventana, username):
        self.ventana = ventana
        self.event = CTkToplevel(self.ventana)
        self.event.title("App")
        self.event.config(bg="#bfd7ff")
        self.event.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.event.resizable(False, False)
        
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
        self.cursor = self.conexion.cursor()
        
        self.event.geometry("880x600")
        
        
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
        self.conexion.close()
        self.event.destroy()
        self.ventana.deiconify()

    def get_points(self):
        self.cursor.execute(f"SELECT `module2` FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
        ver_points=[]
        for bd in self.cursor:
            ver_points.append(bd[0])
        self.points=ver_points[0]
        print(self.points)
    
#*#-----------------------------------------------------------------------------------------------------------------------

    def mostrar_level(self, enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, a, b, c , d):
        # Asignar valores para el nivel 1
        self.enunciado = enunciado
        self.opcion1 = opcion1
        self.consejo1 = consejo1
        self.opcion2 = opcion2
        self.consejo2 = consejo2
        self.opcion3 = opcion3
        self.consejo3 = consejo3
        self.opcion4 = opcion4
        self.consejo4 = consejo4
        self.nivel_actual = nivel_actual
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
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
                            font=("Arial", 24),
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
                            command=lambda: self.actualizar_label(self.consejo1, a, b , c, d),
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
                            command=lambda: self.actualizar_label(self.consejo2, a, b, c, d),
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
                            command=lambda: self.actualizar_label(self.consejo3, a, b, c, d),
                            border_color="white",
                            border_width=3,
                            hover_color="#B8F25D")
        self.boton_c.pack(side="left", padx=(15,0))

        self.boton_d = CTkButton(frame3,
                            text=self.opcion4,
                            bg_color=self.primary_color,
                            fg_color=self.primary_color,
                            text_color="black",
                            font=("Arial", 18),
                            width=280,
                            height=130,
                            anchor="center",
                            command=lambda: self.actualizar_label(self.consejo4, a, b, c, d),
                            border_color="white",
                            border_width=3,
                            hover_color="#B8F25D")
        self.boton_d.pack(side="right", padx=15)

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
            
            self.cursor.execute(f"UPDATE `btibyrq3spz8nqhn2drh`.`users` SET `module2` = '{self.nivel_actual}' WHERE (`username` = '{self.username}');")
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
                self.event.destroy()

#*#-----------------------------------------------------------------------------------------------------------------------
    def mostrar_level_1(self):
        enunciado = "Hay un concierto muy esperado por la ciudad al cual quieres asistir también. Cuando llegas al lugar, te das cuenta de que está repleto de personas por todas partes, todas emocionadas por ver el concierto tomar\ninicio. Asume que fuiste al concierto con una cantidad considerable de cosas importantes (teléfono, billetera, etc)¿Qué acciones tomarías durante la duración del concierto?"
        opcion1 = "Prefiero seguir disfrutandolo\nnormalmente, es un evento\nque quiza lo vea una\nsola vez en la vida"
        consejo1 = "1"
        opcion2 = "Me alejare de las masas,\naunque no pueda ver tanto\na los cantantes en el escenario,\nsiento que será lo mejor para\nevitar un hurto."
        consejo2 = "1"
        opcion3 = "Llamaré a alguien de confianza,\nle dejaré mis cosas y trataré\nde convencerlo para que\nme recoja."
        consejo3 = "1"
        opcion4 = "Siento que es una mala idea,\nes una pena, pero creo que un\nconcierto es simplemente muy\npeligroso para mis pertenencias."
        consejo4 = "1"
        nivel_actual = 1
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 1, 2, 0)

    def mostrar_level_2(self):
        enunciado = "Fuiste invitado a una fiesta de cumpleaños de un conocido tuyo, sin embargo te enteraste de que el lugar donde será realizada la fiesta tiene fama de ser uno donde abundan las pandillas. Aún estas a tiempo de rechazar la oferta o planificar algo para el día de la fiesta en caso de que vayas.¿Que harás?"
        opcion1 = "Es muy peligroso, prefiero\nprevenir que lamentar,\ndiré que estoy enfermo\no algo y no iré."
        consejo1 = "1"
        opcion2 = "Este tipo de lugares\nson cosa común por aquí,\nes probable igual que\nno me pase nada, iré\ncomo si no fuera\nla gran cosa."
        consejo2 = "1"
        opcion3 = "Llamaré a un amigo para\nver si se anima a venir conmigo\n, es mejor estar acompañado\nque solo."
        consejo3 = "1"
        opcion4 = "NADA"
        consejo4 = "1"
        nivel_actual = 2
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 1, 2, 0)

    def mostrar_level_3(self):
        enunciado = "Sales de un concierto, estando ya en una hora avanzada de la noche, y bastante lejos de casa, debes de plantearte la mejor forma de volver a tu casa sin sufrir un percance en el camino de vuelta, ¿Qué harías?"
        opcion1 = "Llamas a un amigo\npara que te recoja."
        consejo1 = "1"
        opcion2 = "Pides un taxi\npara poder volver\na tu casa."
        consejo2 = "1"
        opcion3 = "Pasaras la noche\nen un hotel cercano."
        consejo3 = "1"
        opcion4 = "Tomas el riesgo y\ncaminas hasta la\nestación de buses\nmás cercana."
        consejo4 = "1"
        nivel_actual = 3
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 1, 2, 0)

    def mostrar_level_4(self):
        enunciado = "Te encuentras en una fiesta con unos amigos, es muy tarde y ha pasado ya bastante tiempo desde que inició, a este punto parece que la fiesta ya va a acabar.n En un momento se te acerca un grupo de personas invitando a tu grupo a ir a un lugar que conocen para seguir la fiesta. Tu grupo acepta la propuesta, pero esperan a lo que tengas que decir.¿Qué haces?"
        opcion1 = "Aceptas la invitación\ny te unes a ellos."
        consejo1 = "1"
        opcion2 = "La rechazas, es muy\nriesgoso continuar así\na estas horas de\nla noche."
        consejo2 = "1"
        opcion3 = "Los acompañas, pero\nsólo si un amigo tuyo\nse ofrece a acompañarte\nde vuelta a casa."
        consejo3 = "1"
        opcion4 = "Vas con ellos, pero\nte quedas solo un poco\ny te vas lo más\ntemprano que puedas."
        consejo4 = "1"
        nivel_actual = 4
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 1, 2, 0)

    def mostrar_level_5(self):
        enunciado = "Un festival muy importante está a punto de ocurrir en tu ciudad, se prevee que mucha gente asistirá y que, por lo tanto, las calles estarán repletas de bandas musicales, grupos de artistas, y personas en general. Piensas asistir a este maravilloso evento local, pero te preocupa que seas víctima de un hurto o robo durante tu visita. ¿Qué medidas tomarías para poder disfrutar de este festival de forma segura sin perder la diversión que participar toma?"
        opcion1 = "Prefiero no exponerme\nal más minimo peligro,\nasí que preferiré no ir."
        consejo1 = "1"
        opcion2 = "No podré comprar muchas\ncosas en el festival,\npero prefiero andar con\npoco dinero a que\nandar con mucho."
        consejo2 = "1"
        opcion3 = "Iré acompañado de alguien\n, así quizá las chances\nde que algo ocurra\ndisminuyan."
        consejo3 = "1"
        opcion4 = "Quiero comprar muchas cosas\n, pero para evitar u hurto\nevitare quedarme\nmucho tiempo en el festival."
        consejo4 = "1"
        nivel_actual = 5
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 1, 2, 0)

    def mostrar_level_6(self):  
        enunciado = "Durante tu visita a una feria local de la ciudad, lograste percartarte de que tu celular ya no estaba en tu bolsillo. Haciendo suposiciones, lo más probable es que fuiste víctima de un hurto, y que no fue hace mucho tiempo, quizá si actues bien seas capaz de recuperar tu celular. Pero, ¿Qué Haras?"
        opcion1 = "Buscaré la ayuda de\nun agente de la\npolicía/serenazgo."
        consejo1 = "1"
        opcion2 = "Dudo que las autoridades\nme ayuden, trataré de\nbuscar al ladrón\nyo mismo."
        consejo2 = "1"
        opcion3 = "Lo hecho ya está hecho\n, no desperdiciaré mis\nenergías en una\npersecusión sin sentido."
        consejo3 = "1"
        opcion4 = "Llamaré la atención de\nlas personas, quizá ellos\nme ayuden a encontrar\nal culpable."
        consejo4 = "1"
        nivel_actual = 6
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 1, 2, 0)


        
    def widgets(self):
        
        carpeta_principal = os.path.dirname(__file__)
        carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")

        
        frame_derecho = CTkFrame(self.event, width=640, fg_color=self.primary_color, corner_radius=0)
        frame_derecho.pack(side="right", fill="both", expand=True)
        frame_derecho.pack_propagate(False)
        
        
        self.frame_derecho = frame_derecho  # Guardar referencia al frame derecho
        
        frame_izquierdo = CTkFrame(self.event, fg_color=self.third_color, corner_radius=0, width=240)
        frame_izquierdo.pack(side="left", fill="y")
        frame_izquierdo.pack_propagate(False)
        
        imagen_autobus = CTkImage(Image.open(os.path.join(carpeta_imagenes, "calendario.png")), size=(150, 130))
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

if __name__ == "__main__":
    root = CTk()
    
    username = "Miguel"
    
    trans = Eventmodule(root)
    
    
    root.mainloop()