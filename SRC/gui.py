import customtkinter as ctk
from PIL import Image, ImageTk
import os
from main import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Joysthing")
app.geometry("800x600")

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "..", "assets", "img", "joystick.png")

background_image = Image.open(image_path)
background_image = background_image.resize((800, 600))
bg_image = ImageTk.PhotoImage(background_image)

background_label = ctk.CTkLabel(app, image=bg_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

boton_A = ctk.CTkButton(app, text="X", command=lambda: elegir_tecla("X"), corner_radius=45,width=50, font=("",25))
boton_A.place(x=620, y=225)

boton_B = ctk.CTkButton(app, text="○", command=lambda: print("Boton B"), corner_radius=45,width=50, font=("",25))
boton_B.place(x=675, y=185)

boton_X = ctk.CTkButton(app, text="□", command=lambda: print("Boton X"), corner_radius=45,width=50, font=("",25))
boton_X.place(x=565, y=185)

boton_Y = ctk.CTkButton(app, text="△", command=lambda: print("Boton Y"), corner_radius=45,width=50, font=("",25))
boton_Y.place(x=620, y=150)

def abrir_config():
    ventana_config = ctk.CTkToplevel(app)
    ventana_config.title("Configuracion")
    ventana_config.geometry("400x300")

    label = ctk.CTkLabel(ventana_config, text="Configuraciones", font=("Arial", 20))
    label.pack(pady=20)

    ctk.CTkSwitch(ventana_config, text="Modo oscuro").pack(pady=10)
    ctk.CTkButton(ventana_config, text="Guardar").pack(pady=10)

boton_config = ctk.CTkButton(app, text="⚙️", width=40, command=abrir_config)
boton_config.place(x=750, y=10)

app.mainloop()
