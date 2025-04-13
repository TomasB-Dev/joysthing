import customtkinter as ctk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from main import elegir_tecla, Listar_Dispositivo, pyautogui, seleccionar_dispositivos, modify_dispo, seleccionado, cargar_configuracion

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "..", "assets", "img", "joystick.png")
logo_path = os.path.join(base_path, "..", "assets", "img", "logo.ico")

app = ctk.CTk()
app.iconbitmap(logo_path)
app.title("Joysthing")
app.geometry("800x600")

background_image = Image.open(image_path).resize((800, 600))
bg_image = ImageTk.PhotoImage(background_image)
background_label = ctk.CTkLabel(app, image=bg_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

tecla_actual = None

ESTILO_BOTON = {
    "corner_radius": 45,
    "width": 50,
    "font": ("Segoe UI", 20, "bold"),
    "hover_color": "#dbc604"
}

ESTILO_BOTON_PEQUENO = {
    "corner_radius": 45,
    "width": 70,
    "font": ("Segoe UI", 12, "bold"),
    "hover_color": "#dbc604"
}

def iniciar_escucha_tecla(ubicacion):
    Dispositivo_selected = seleccionado()
    if Dispositivo_selected is None:
        messagebox.showerror("Error", "Debes seleccionar el dispositivo en configuracion.\nSi el error continua, comuniquese con soporte.")
    else:
        global tecla_actual
        tecla_actual = ubicacion
        app.focus_set()

def tecla_presionada(event):
    if tecla_actual is not None:
        elegir_tecla(tecla_actual, event.keysym)

def crear_boton(texto, tecla, x, y, estilo=ESTILO_BOTON):
    boton = ctk.CTkButton(app, text=texto, command=lambda: iniciar_escucha_tecla(tecla), **estilo)
    boton.place(x=x, y=y)
    return boton

#principales
crear_boton("X", 0, 620, 225)
crear_boton("O", 1, 675, 185)
crear_boton("■", 2, 565, 185)
crear_boton("△", 3, 620, 150)
#gatillos
crear_boton("R1", 5, 620, 100)
crear_boton("R2", 7, 620, 50)
crear_boton("L1", 4, 120, 100)
crear_boton("L2", 6, 120, 50)
#select start
crear_boton("START", 8, 520, 120, estilo=ESTILO_BOTON_PEQUENO)
crear_boton("SELECT", 9, 210, 120, estilo=ESTILO_BOTON_PEQUENO)

#flechas
crear_boton("▲", 10, 125, 160, estilo=ESTILO_BOTON_PEQUENO)
crear_boton("▼", 13, 125, 220, estilo=ESTILO_BOTON_PEQUENO)
crear_boton("❰", 12, 90, 190, estilo=ESTILO_BOTON_PEQUENO)
crear_boton("❱", 11, 165, 190, estilo=ESTILO_BOTON_PEQUENO)
#analogicos
crear_boton("up",14,250,250, estilo=ESTILO_BOTON_PEQUENO)

def abrir_config():
    ventana_config = ctk.CTkToplevel(app)
    ventana_config.title("Configuracion")
    ventana_config.geometry("400x300")
    ventana_config.lift()
    ventana_config.focus_force()
    ventana_config.attributes("-topmost", True)

    label = ctk.CTkLabel(ventana_config, text="Configuraciones", font=("Arial", 20))
    label.pack(pady=20)

    ctk.CTkSwitch(ventana_config, text="Modo oscuro").pack(pady=10)

    dispositivos = seleccionar_dispositivos()
    label_dipositivo = ctk.CTkLabel(ventana_config, text="Dispositivo", font=("Arial", 20))
    label_dipositivo.pack(pady=10)

    seleccionar = ctk.CTkOptionMenu(ventana_config, values=dispositivos)
    seleccionar.pack(pady=10)

    ctk.CTkButton(ventana_config, text="Guardar", command=lambda: modify_dispo(seleccionar.get())).pack(pady=10)

boton_config = ctk.CTkButton(app, text="⚙️", width=40, command=abrir_config)
boton_config.place(x=750, y=10)

def al_cerrar():
    app.destroy()
    pyautogui.press('enter')

app.bind("<Key>", tecla_presionada)
app.protocol("WM_DELETE_WINDOW", al_cerrar)
cargar_configuracion()
app.mainloop()
