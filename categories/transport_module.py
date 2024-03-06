from customtkinter import *


class TransportModule:
    def __init__(self, master):
        self.root = CTkToplevel(master)
        self.root.grab_set()
        self.root.geometry("600x600")
        self.root.minsize(600, 600)
        self.root.config(bg="#FFFFFF")
        
        self.widgets()

    def widgets(self):
        upper_frame = CTkFrame(
            self.root,
            fg_color="#CCCCCC",
            bg_color="#CCCCCC",
            height=85
        )
        upper_frame.pack(fill="x", expand=True, side="top", pady=0)
