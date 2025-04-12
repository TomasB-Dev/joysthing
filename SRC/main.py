from pywinusb import hid
import pyautogui
import threading
import json
last_join = [""] * 2 #funciona en base a los campos 6 es el primero, gatillos 2do
teclas=[ 79 , # X
        47, # CIRCULO
        143, # CUADRADO
        31, # TRIANGULO
        1, #l1
        2, #r1
        4, #l2
        8, #r2
        32,#START
        16,#SELECT
        #flechas 
        0, #up
        11, #derecha
        6,# left
        4, #down
        #end flechas
        ]
tecla_elegida = [""] * 20 #momentaneo
Dispositivo_selected = None
#cargar/guardar info
def guardar_configuracion():
    config = {
        "teclas": tecla_elegida,
    }
    with open("config.json", "w") as archivo:
        json.dump(config, archivo)
    print("configuracion guardada")
def cargar_configuracion():
    global tecla_elegida, Dispositivo_selected
    try:
        with open("config.json", "r") as archivo:
            config = json.load(archivo)
            tecla_elegida = config.get("teclas", [""] * 20)          
    except FileNotFoundError:
        print("no se encontro un archivo de configuracion.")


def handler(datos_raw):
    """
    mostrar info array de botones, place 6 contiene los btns del cuadrado, ciruclo, triangulo y x
    """
    if datos_raw[6] > 15 and datos_raw[3] < 115 or datos_raw[3] > 130 : #esto para controlar el spam de mi joystick no necesario
        print("Raw data:", datos_raw) # para ver que pocion tiene
    boton_data = datos_raw[6]
    gatillos_btn = datos_raw[7]
    #buscar / pensar una manera mas eficiente de hacer esto
    # btn principales xov
    if boton_data == 79 and last_join[0] != 79: # la x
        last_join[0] = 79
        pyautogui.press(f'{tecla_elegida[0]}')
    elif boton_data == 47 and last_join[0] != 47: # circulo
        last_join[0] = 47
        pyautogui.press(f'{tecla_elegida[1]}')
    elif boton_data == 143 and last_join[0] != 143: # cuadrado
        last_join[0] = 143
        pyautogui.press(f'{tecla_elegida[2]}')
    elif boton_data == 31 and last_join[0] != 31: # triangulo
            last_join[0] = 31
            pyautogui.press(f'{tecla_elegida[3]}')
    #FLECHAS (estan en la misma freq que los principales)
    elif boton_data == 0 and last_join[0] != 0: # up
            last_join[0] = 0
            pyautogui.press(f'{tecla_elegida[10]}')
    elif boton_data == 2 and last_join[0] != 2: # derecha
            last_join[0] = 2
            pyautogui.press(f'{tecla_elegida[11]}')
    elif boton_data == 6 and last_join[0] != 6: # left
            last_join[0] = 6
            pyautogui.press(f'{tecla_elegida[12]}')
    elif boton_data == 4 and last_join[0] != 4: # down
            last_join[0] = 4
            pyautogui.press(f'{tecla_elegida[13]}')
    #reasigna el estado de lastjoin
    elif boton_data != last_join[0]:
        last_join[0] = boton_data
    #GATILLOS

    if gatillos_btn == 1 and last_join[1] != 1:#l1
        last_join[1] = 1
        pyautogui.press(f'{tecla_elegida[4]}')
    if gatillos_btn == 2 and last_join[1] != 2:#r1
        last_join[1] = 2
        pyautogui.press(f'{tecla_elegida[5]}')
    if gatillos_btn == 4 and last_join[1] != 4:#l2
        last_join[1] = 4
        pyautogui.press(f'{tecla_elegida[6]}')
    if gatillos_btn == 8 and last_join[1] != 8:#r2
        last_join[1] = 8
        pyautogui.press(f'{tecla_elegida[7]}')
    elif gatillos_btn != last_join[1]:
        last_join[1] = gatillos_btn
def elegir_tecla(ubicacion,data):
    """selecciona la tecla elegida y la guarda en el espacio correspondiente"""
    tecla_elegida[ubicacion] = data
    guardar_configuracion()



def Listar_Dispositivo():
    """
    funcion principal, se encarga de mantener abierto el dispositivo
    """
    
    dispositivos = hid.HidDeviceFilter().get_devices()
    for dispositivo in dispositivos:
        if dispositivo.product_name == Dispositivo_selected:
            dispositivo.open()
            dispositivo.set_raw_data_handler(handler)
            input()
            dispositivo.close()

    
    

def seleccionar_dispositivos():
    """
    devuelve los nombres de los dispositivos para listarlos en la seleccion
    """
    dispositivos = hid.HidDeviceFilter().get_devices()
    nombres_dispositivos = [""]
    for dispositivo in dispositivos:
        if dispositivo.product_name != "USB DEVICE": #ajenos a ser joyctiks
            nombres_dispositivos.append(dispositivo.product_name)
    return nombres_dispositivos

def modify_dispo(selected):
    """
    Modifica el dispositivo seleccionado
    """
    global Dispositivo_selected
    Dispositivo_selected = selected
    guardar_configuracion()
    thread = threading.Thread(target=Listar_Dispositivo, daemon=True)
    thread.start()    

def seleccionado():
    "devuelve si hay dispositivo seleccionado"
    return Dispositivo_selected
