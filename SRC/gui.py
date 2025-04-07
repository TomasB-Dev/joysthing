import customtkinter as ctk
from PIL import Image, ImageTk
import os
import threading
from main import elegir_tecla, Listar_Dispositivo, pyautogui,seleccionar_dispositivos

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "..", "assets", "img", "joystick.png")
logo_path = os.path.join(base_path,"..", "assets", "img", "logo.ico")

app = ctk.CTk()
app.iconbitmap(logo_path)
app.title("Joysthing")
app.geometry("800x600")

tecla_actual = None

def iniciar_escucha_tecla(ubicacion):
    global tecla_actual
    tecla_actual = ubicacion
    app.focus_set()

def tecla_presionada(event):
    if tecla_actual is not None:
        elegir_tecla(tecla_actual, event.keysym)
        print("entre")



background_image = Image.open(image_path)
background_image = background_image.resize((800, 600))
bg_image = ImageTk.PhotoImage(background_image)

background_label = ctk.CTkLabel(app, image=bg_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

boton_A = ctk.CTkButton(app, text="X", command=lambda: iniciar_escucha_tecla(0), corner_radius=45, width=50, font=("", 25))
boton_A.place(x=620, y=225)

boton_B = ctk.CTkButton(app, text="O", command=lambda: iniciar_escucha_tecla(1), corner_radius=45, width=50, font=("", 25))
boton_B.place(x=675, y=185)

boton_X = ctk.CTkButton(app, text="■", command=lambda: iniciar_escucha_tecla(2), corner_radius=45, width=50, font=("", 25))
boton_X.place(x=565, y=185)

boton_Y = ctk.CTkButton(app, text="△", command=lambda: iniciar_escucha_tecla(3), corner_radius=45, width=50, font=("", 25))
boton_Y.place(x=620, y=150)

boton_r1 = ctk.CTkButton(app, text="R1", command=lambda: iniciar_escucha_tecla(5), corner_radius=45, width=50, font=("", 25))
boton_r1.place(x=620, y=100)

boton_r2 = ctk.CTkButton(app, text="R2", command=lambda: iniciar_escucha_tecla(7), corner_radius=45, width=50, font=("", 25))
boton_r2.place(x=620, y=50)

boton_l1 = ctk.CTkButton(app, text="L1", command=lambda: iniciar_escucha_tecla(4), corner_radius=45, width=50, font=("", 25))
boton_l1.place(x=120, y=100)

boton_r2 = ctk.CTkButton(app, text="L2", command=lambda: iniciar_escucha_tecla(6), corner_radius=45, width=50, font=("", 25))
boton_r2.place(x=120, y=50)

boton_start = ctk.CTkButton(app, text="START", command=lambda: iniciar_escucha_tecla(8), corner_radius=45, width=40, font=("", 12))
boton_start.place(x=520, y=120)

boton_select = ctk.CTkButton(app, text="SELECT", command=lambda: iniciar_escucha_tecla(9), corner_radius=45, width=40, font=("", 12))
boton_select.place(x=210, y=120)
#flechas
boton_f_up = ctk.CTkButton(app, text="▲", command=lambda: iniciar_escucha_tecla(10), corner_radius=45, width=40, font=("", 12))
boton_f_up.place(x=125, y=160)

boton_f_down = ctk.CTkButton(app, text="▼", command=lambda: iniciar_escucha_tecla(13), corner_radius=45, width=40, font=("", 12))
boton_f_down.place(x=125, y=220)

boton_f_left = ctk.CTkButton(app, text="❰", command=lambda: iniciar_escucha_tecla(12), corner_radius=45, width=40, font=("", 12))
boton_f_left.place(x=90, y=190)

boton_f_ri = ctk.CTkButton(app, text="❱", command=lambda: iniciar_escucha_tecla(11), corner_radius=45, width=40, font=("", 12))
boton_f_ri.place(x=165, y=190)
def abrir_config():
    ventana_config = ctk.CTkToplevel(app)   
    ventana_config.title("Configuracion")
    ventana_config.geometry("400x300")
    #focus ventana
    ventana_config.lift()
    ventana_config.focus_force()
    ventana_config.attributes("-topmost", True)
    #end focus
    label = ctk.CTkLabel(ventana_config, text="Configuraciones", font=("Arial", 20))
    label.pack(pady=20)

    ctk.CTkSwitch(ventana_config, text="Modo oscuro").pack(pady=10)  
    dispositivos = seleccionar_dispositivos()
    label_dipositivo = ctk.CTkLabel(ventana_config, text="Dispositivo", font=("Arial", 20))
    label_dipositivo.pack(pady=10)
    seleccionar = ctk.CTkOptionMenu(ventana_config, values=dispositivos, )
    seleccionar.pack(pady=10)
    ctk.CTkButton(ventana_config, text="Guardar").pack(pady=10)

boton_config = ctk.CTkButton(app, text="⚙️", width=40, command=abrir_config)

boton_config.place(x=750, y=10)
#hilo en segundo plano para poder seguir ejecutando el script
thread = threading.Thread(target=Listar_Dispositivo, daemon=True)
thread.start()
def al_cerrar():
    app.destroy()
    pyautogui.press('enter')
    
app.bind("<Key>", tecla_presionada)
app.protocol("WM_DELETE_WINDOW", al_cerrar)
app.mainloop()
