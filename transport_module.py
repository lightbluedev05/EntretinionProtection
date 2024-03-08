from tkinter import messagebox
from customtkinter import *
from PIL import Image
import os
import mysql.connector

#.
class TransportModule:
    def __init__(self, ventana, username):
        self.ventana = ventana
        self.transport = CTkToplevel(self.ventana)
        self.transport.title("App")
        self.transport.config(bg="#bfd7ff")
        self.transport.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.transport.resizable(False, False)
        
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
        
        self.transport.geometry("880x600")
        
        
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
        self.transport.destroy()
        self.ventana.deiconify()
        

    def get_points(self):
        self.cursor.execute(f"SELECT `module1` FROM btibyrq3spz8nqhn2drh.users WHERE `username`= '{self.username}'")
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
            
            self.cursor.execute(f"UPDATE `btibyrq3spz8nqhn2drh`.`users` SET `module1` = '{self.nivel_actual}' WHERE (`username` = '{self.username}');")
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
                self.transport.destroy()

#*#-----------------------------------------------------------------------------------------------------------------------
    def mostrar_level_1(self):
        enunciado = "Imagina que estás en un largo viaje en autobús o tren, rodeado de otros pasajeros. De repente, un individuo armado entra en el vehículo y se dirige hacia ti, exigiendo tus pertenencias. ¿Qué acciones tomarías en este momento para protegerte a ti mismo y a los demás pasajeros del peligro?"
        opcion1 = "Entregar tus pertenencias,\ny automaticamente avisar\nal conductor de cerrar\nlas puertas"
        consejo1 = "Si has optado por esta respuesta, dejame decirte que parece ser una buena opción al entregar tus pertenencias sin ejercer presión, pero debemos percatarnos que al estar armado, el podría alterar contra la vida no solo tuya , sino del conductor y los civiles que se encuentran en el bus."
        opcion2 = "Mantener la calma y entregar\ntus pertenencias y esperar\nque nadie este en peligro\npara avisar de que\nel ladrón tiene un arma"
        consejo2 = "Exacto,es importante mantener la calma en ese momento y ceder ante cualquier robo a mano armada, una vez que el atraco haya terminado y el agresor ya no represente una amenaza inmediata, busca la oportunidad de comunicar discretamente al conductor la situación"
        opcion3 = "Resistir al atraco y gritar\nque te estan robando "
        consejo3 = "Si te encuentras en esta situación, es crucial que priorices tu seguridad y la de los demás pasajeros. No intentes resistir al atraco si el agresor está armado, ya que esto puede poner en peligro tu vida y la de los demás."
        nivel_actual = 1
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 1, 0, 2)
        
    def mostrar_level_2(self):
        enunciado = "Imagina que estás en un autobús lleno de gente, viajando hacia tu destino. De repente, notas que alguien cerca de ti comienza a acosarte verbal o físicamente. Te sientes incómodo y alarmado por la situación. ¿Qué acciones tomarías en este momento para protegerte a ti mismo y enfrentar esta situación de acoso en el transporte público?"
        opcion1 = "Ignorar al acosador\ny cambiar de asiento\nsi es posible."
        consejo1 = "Si bien cambiar de asiento puede ayudarte a alejarte físicamente del acosador, simplemente ignorarlo puede no resolver el problema subyacente. Ignorar el acoso puede dar la impresión al acosador de que su comportamiento es aceptable o que no está teniendo un impacto negativo en ti o en otros pasajeros"
        opcion2 = "Reportar el incidente\nal llegar a tu\ndestino."
        consejo2 = "Parece una buena alternativa, pero al tener poquisima información del acosador, probablemente no podrías llegar a nada"
        opcion3 = "Confrontar  al acosador\ny establecer límites claros\nsobre tu espacio personal."
        consejo3 = "Excelente elección. Confrontar al acosador de manera educada pero firme es una forma efectiva de hacerle saber que su comportamiento no es aceptable y establecer límites claros para proteger tu espacio personal	Al enfrentarlo de esta manera, estás defendiendo tus derechos y promoviendo un ambiente de respeto en el transporte público."
        nivel_actual = 2
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 1, 0, 2)

    def mostrar_level_3(self):
        enunciado = " Imagina que estás en un autobús lleno de gente cuando de repente dos pasajeros comienzan a discutir acaloradamente por un asiento. La situación escalada rápidamente y ahora están empujándose y gritándose mutuamente."
        opcion1 = "Llamar a la policía"
        consejo1 = "Esta es una acción crucial y totalmente correcta en situaciones de pelea o violencia en el transporte público. Llamar a la policía puede garantizar una intervención rápida y profesional para resolver la situación de manera segura y legal."
        opcion2 = "Tratar de calmar la\nsituación mediando entre\nlas partes"
        consejo2 = "Si bien intentar calmar la situación puede ser noble, también puede ser arriesgado y potencialmente peligroso si no estás entrenado para manejar conflictos. Es mejor dejar la mediación a profesionales capacitados, como el personal del transporte o las autoridades, para garantizar que la situación se resuelva de manera segura y efectiva"
        opcion3 = "Grabar la situación\ny reportarla a redes"
        consejo3 = "Grabar la situación puede proporcionar evidencia útil para las autoridades y ayudar a identificar a los responsables. Sin embargo, es importante priorizar la seguridad personal y buscar ayuda profesional en lugar de depender únicamente de las redes sociales para resolver la situación."
        nivel_actual = 3
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 0, 1, 2)

    def mostrar_level_4(self):
        enunciado = "Imagina que estás viajando en un taxi cuando el conductor cambia repentinamente de ruta y se desvía hacia un área poco transitada. Comienzas a sentirte incómodo/a y sospechas que el conductor pueda tener intenciones maliciosas."
        opcion1 = "Pedirle al conductor que\nte lleve de vuelta\nal punto de origen y\nsalir del taxi en\ncuanto sea posible:"
        consejo1 = "Pedirle al conductor que te lleve de vuelta al punto de origen y salir del taxi en cuanto sea posible: Es importante mantener la calma y tratar de no mostrar signos de pánico mientras solicitas al conductor que regrese al punto de origen."
        opcion2 = "Llamar a la policía y\nproporcionarles la ubicación\nactual del taxi y cualquier\ndetalle relevante sobre\nel conductor."
        consejo2 = "Llamar a la policía y proporcionarles la ubicación actual del taxi y cualquier detalle relevante sobre el conductor. Llamar a las autoridades es una medida crucial para obtener ayuda profesional y garantizar una intervención rápida y efectiva para resolver la situación de manera segura."
        opcion3 = "Intentar luchar contra\nel conductor y escapar\ndel taxi por cualquier\nmedio necesario."
        consejo3 = "Intentar luchar contra el conductor y escapar del taxi por cualquier medio necesario. Esta respuesta aumentaría el riesgo de violencia y daño físico tanto para ti como para el conductor, y podría empeorar la situación."
        nivel_actual = 4
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 0, 1, 2)

    def mostrar_level_5(self):
        enunciado = " Estás en un autobús urbano cuando un grupo de individuos armados aborda el vehículo y comienza a exigir dinero y pertenencias a los pasajeros. La situación se vuelve cada vez más tensa y temes por tu seguridad y la de los demás pasajeros."
        opcion1 = "Esperar pasivamente a que\nla situación se resuelva\npor sí sola."
        consejo1 = "Si decides esperar pasivamente, asegúrate de mantenerte alerta y observar cuidadosamente la situación en busca de cualquier cambio o desarrollo. Utiliza este tiempo para evaluar tus opciones y prepararte para tomar medidas si la situación empeora. Por ejemplo, identifica salidas de emergencia o posibles rutas de escape en caso de ser necesario."
        opcion2 = "Llamar a la policía o emergencias\ny proporcionarles la ubicación\nactual del autobús y\ncualquier detalle relevante\nsobre los secuestradores."
        consejo2 = "Llamar a las autoridades es crucial en situaciones de secuestro, ya que pueden proporcionar ayuda profesional y coordinar una respuesta adecuada para garantizar la seguridad de los pasajeros y resolver la situación de manera segura."
        opcion3 = "Tratar de resistir físicamente\ny luchar contra los\nsecuestradores para escapar\ndel autobús."
        consejo3 = "Esta acción aumentaría significativamente el riesgo de violencia y podría poner en peligro la seguridad tanto de los pasajeros como de los secuestradores."
        nivel_actual = 5
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 0, 1, 2)

    def mostrar_level_6(self):  
        enunciado = "Has solicitado un viaje en Uber y, durante el trayecto, el conductor detiene el vehículo en un lugar aislado y exige que entregues todas tus pertenencias."
        opcion1 = "Esperar  a que la\nsituación se resuelva\npor sí sola."
        consejo1 = "Recuerda que la pasividad puede no ser la mejor opción en situaciones de peligro. Siempre es recomendable buscar ayuda profesional y contactar a las autoridades lo antes posible."
        opcion2 = "Llamar a la policía y\nproporcionarles la ubicación\nactual del autobús y\ncualquier detalle relevante\nsobre los secuestradores"
        consejo2 = "Llamar a las autoridades de inmediato es la acción más adecuada en situaciones de secuestro. Proporciona a la policía toda la información disponible, incluida la ubicación del autobús y cualquier detalle relevante sobre los secuestradores."
        opcion3 = "Tratar de resistir\nfísicamente y luchar contra\nlos secuestradores para escapar\ndel autobús."
        consejo3 = "Resistir físicamente puede aumentar el riesgo de violencia y poner en peligro la seguridad de los pasajeros	 Es mejor evitar cualquier confrontación directa y buscar ayuda profesional llamando a la policía"
        nivel_actual = 6
        
        self.mostrar_level(enunciado, opcion1, consejo1, opcion2, consejo2, opcion3, consejo3, nivel_actual, 0, 1, 2)

        
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
    
    trans = TransportModule(root)
    
    
    root.mainloop()