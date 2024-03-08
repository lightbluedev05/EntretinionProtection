from tkinter import messagebox
from customtkinter import *
from PIL import Image
import os
import mysql.connector

#.
class CalleModule:
    def __init__(self, ventana, username):
        self.ventana = ventana
        self.call = CTkToplevel(self.ventana)
        self.call.title("App")
        self.call.config(bg="#bfd7ff")
        self.call.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.call.resizable(False, False)
        
        self.username = username
        
        #$####### MYSQL CONNECTION ############
        host="btibyrq3spz8nqhn2drh-mysql.services.clever-cloud.com"
        user="uklu2xhrdmj6v1w9"
        password="n9N3OZ7LHYaH6D7VFYqZ"
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        self.cursor = self.conexion.cursor()
        
        self.call.geometry("880x600")
        
        
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
        
#
    def cerrar_ventana(self):
        self.conexion.close()
        self.call.destroy()
        self.ventana.deiconify()
        

    def get_points(self):
        self.cursor.execute(f"SELECT `module3` FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
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
                            font=("Arial", 20),
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
        frame3.pack(fill="x", pady=5)

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
                                    text_color="black",
                                    font=("Arial", 20),
                                    height=100,
                                    wraplength=610)
        self.label_texto.pack(fill="x", side="bottom", pady=5)

    def actualizar_label(self, texto, *botones):
        
        colores = {0: "#7CB679", 1: "#CCD06F", 2: "#D0726F"}

        for i, boton in enumerate(botones, start=1):
            color = colores.get(boton, "#7CB679")
            
            getattr(self, f"boton_{chr(96 + i)}").configure(
                fg_color=color, hover_color=color, command=None
            )

        self.label_texto.configure(text=texto)
        
        
        if self.points < self.nivel_actual:
            
            self.cursor.execute(f"UPDATE `btibyrq3spz8nqhn2drh`.`users` SET `module3` = '{self.nivel_actual}' WHERE (`username` = '{self.username}');")
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
                self.call.destroy()

#*#-----------------------------------------------------------------------------------------------------------------------
    def mostrar_level_1(self):
        enunciado = "Quedaste con un amigo en su casa, pero se te pasó la hora y ya es de noche. Tienes algo urgente que hacer en tu casa, así que tienes que volver rápido. ¿Qué ruta tomarías para llevar a cabo esta tarea de la forma más segura posible?"
        opcion1 = "Tomaré un taxi\npara llegar a mi destino"
        consejo1 = "Una buena idea, aunque solo de día, de noche algun taxi falso puede ser el que toque."
        opcion2 = "Caminaré hasta la parada\nde buses más cercana"
        consejo2 = "Es muy arriesgado, ¿No?, ni a menos que estes completamente seguro que nada te pasara esto podría ser algo recomendable."
        opcion3 = "Le pediré a mi amigo que\nme acompañe hasta un lugar\nseguro donde pueda tomar un\ncolectivo"
        consejo3 = "Buena idea, aunque expones a tu amigo al peligro si eliges esta opción, ya que el tendrá que volver solo."
        opcion4 = "Usaré una aplicación de\ntaxi para que me\nlleve hasta mi casa"
        consejo4 = "Estas aplicaciones suelen estar más reguladas, así que hay menos chance de que algo ocurra, sin embargo, nunca bajes la guardia."
        nivel_actual = 1
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 1, 2, 1, 0)
        
    def mostrar_level_2(self):
        enunciado = "Estás caminando por la calle cuando presencias un robo ocurriendo a poco menos de una cuadra de ti, estando tan cerca, ¿Qué deberías hacer?"
        opcion1 = "Lo ignoraré y me\nalejaré del lugar."
        consejo1 = "Es algo inteligente sin lugar a dudas, aunque dejar un acto así ignorado quiza no sea la mejor opción."
        opcion2 = "Trataré de ayudar."
        consejo2 = "Te estas exponiendo a mucho riesgo, no sabes is hay complices esperando, asi que mejor sería no acercarte."
        opcion3 = "Gritaré por ayuda,\npero me mantendré\nlejos."
        consejo3 = "Puede funcionar, pero depende mucho de la zona, aparte, incluso estando lejos, llamando la atención de esta forma, puedes correr riesgos."
        opcion4 = "Llamaré a la\npolicía/serenazgo, quizá\nellos puedan hacer algo."
        consejo4 = "Aunque no lo parezca, esto puede ayudar mucho, si bien el crimen no será detenido al momento, la policía tendra en sus registros este hecho, para poder detener al criminal luego."
        nivel_actual = 2
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 1, 2, 1, 0)

    def mostrar_level_3(self):
        enunciado = "Es de día, pero te percatas de un pequeño grupo de personas que parece seguirte en tu recorrido ¿Qué harás?"
        opcion1 = "Tomar un bus/colectivo/taxi\npara perderlos."
        consejo1 = "Si estamos hablando de un grupo de personas con malas intenciones, tomar un bus/colectivo no los perderá tan facilmente."
        opcion2 = "Seguir caminando normalmente\n, es de día,\nno puede pasar nada malo."
        consejo2 = "Estas siendo desprevenido, a pesar de que sea de día, hay zonas en las que tu camino te puede llevar a ser asaltado."
        opcion3 = "Caminar hasta una\nzona más segura\n(parque, comisaría, etc)."
        consejo3 = "Una de las mejores opciones claramente, el grupo de personas no te seguira hasta un lugar donde ellos se volverían vulnerables."
        opcion4 = "Darte la vuelta\ny confrontarlos."
        consejo4 = "Llamarás innecesariamente la atención, y aparte, peudes meterte en problemas por causar un escándalo en público."
        nivel_actual = 3
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 1, 2, 0, 2)

    def mostrar_level_4(self):
        enunciado = "Caminaste por un callejón y ahora te están robando, tienes pertenencias valiosas en tu mochila que no quieres perder, pero la situación es difícil para ti en este momento. ¿Qué harás?"
        opcion1 = "Gritar y pedir por\nayuda a cualquier persona cerca."
        consejo1 = "Incluso si funciona, hasta que la ayuda llegue, los ladrones pueden ejercer violencia sobre tí, lo cual no es bueno."
        opcion2 = "Tratar de huir lo\nmás rápido que puedas."
        consejo2 = "Podría funcionar, pero no sabes si tienen complices viendo desde lejos, lo cual solo agravaría tu situación aún más."
        opcion3 = "Entregar todo lo que\ntengas por temor a algún\nacto de mayor violencia."
        consejo3 = "Lamentablemente, es la opción más inteligente, lo material es temporal, pero es mejor preservar tu vida/salud que bienes materiales."
        opcion4 = "Tratar de defenderte del robo."
        consejo4 = "Probablemente no salga bien, y aparte te expondras a más peligro combinado con violencia innecesaria."
        nivel_actual = 4
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 1, 2, 0, 2)

    def mostrar_level_5(self):
        enunciado = "Caminando por una calle, una persona, aparentemente ambulante, se acerca a ti insistiéndote en que le compres algo, tratas de ignorarlo, pero el individuo acelera su paso y ahora te insulta, ¿Qué harás?"
        opcion1 = "Seguir ignorándolo esperando\nque pronto se cansará."
        consejo1 = "No sabes como la otra persona reaccionará, pero quizá sea inteligente actuar de esa manera, estando en público es improbable que algo mayor suceda."
        opcion2 = "Confrontarlo e insultarlo\ndevuelta."
        consejo2 = "La otra persona puede reaccionar de una forma más violenta, así que mejor evitar esto."
        opcion3 = "Acelerar el paso y tratar\nde ir a un lugar más seguro o\ncon más gente."
        consejo3 = "Una opción muy inteligente, asegurandote de que la persona se sienta presionada por el público evitara que la persona haga algo."
        opcion4 = "Amenazarlo con llamar\nal serenazgo/policía."
        consejo4 = "Podrías provocarlo innecesariamente, y eso puede acabar de una forma terrible."
        nivel_actual = 5
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 1, 2, 0, 2)

    def mostrar_level_6(self):  
        enunciado = "Mientras volvías a tu casa, una persona te para y te pide que le digas que hora es, para tu mala suerte, no sabes que hora es tampoco, y la única forma de hacerlo sería sacando tu celular para comprobarlo, pero, ante esta situación, ¿Qué harías?"
        opcion1 = "Mentir con una hora falsa."
        consejo1 = "Es una buena forma de evitar que te sigan con su intento, aunque quiza debas planear una ruta de escape en caso vuelvan por más."
        opcion2 = "Acceder al pedido y\ndarle la hora correcta\n(sacar tu celular para ello)."
        consejo2 = "Es muy arriesgado, podrías sufrir un robo en este punto si las personas que te hacen las preguntas son realmente ladrones."
        opcion3 = "Tratar de persuadirlo\npara que te deje ir."
        consejo3 = "Depende mucho de qué tanto puedas persuadirlos, aunque mantener una conversación con ellos quiza no sea una buena idea."
        opcion4 = "Ignorarlo y seguir\ncon tu camino."
        consejo4 = "Puedes provocarlos de este modo, aunque es una buena forma de evitarlos."
        nivel_actual = 6
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, opcion4, consejo4, nivel_actual, 0, 2, 1, 1)

        
    def widgets(self):
        
        carpeta_principal = os.path.dirname(__file__)
        carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")

        
        frame_derecho = CTkFrame(self.call, width=640, fg_color=self.primary_color, corner_radius=0)
        frame_derecho.pack(side="right", fill="both", expand=True)
        frame_derecho.pack_propagate(False)
        
        
        self.frame_derecho = frame_derecho  # Guardar referencia al frame derecho
        
        frame_izquierdo = CTkFrame(self.call, fg_color=self.third_color, corner_radius=0, width=240)
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
            

if __name__ == "__main__":
    root = CTk()
    
    username = "Nashe"
    
    trans = CalleModule(root)
    
    
    root.mainloop()