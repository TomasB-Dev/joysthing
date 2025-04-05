from pywinusb import hid
import pyautogui
last_join = [None]
teclas=[ 79 , # X
        47, # CIRCULO
        143, # CUADRADO
        31, # TRIANGULO
        ]
tecla_elegida = []
def handler(datos_raw):
    """
    mostrar info array de botones, place 6 contiene los btns del cuadrado, ciruclo, triangulo y x
    """
    if datos_raw[6] > 15 and datos_raw[3] < 115 or datos_raw[3] > 130 : #esto para controlar el spam de mi joystick no necesario
        print("Raw data:", datos_raw)
    boton_data = datos_raw[6]
    if boton_data == 79 and last_join[0] != 79: # la x
        last_join[0] = 79
        pyautogui.press(f'{tecla_elegida[0]}')
    elif boton_data == 47 and last_join[0] != 47: # circulo
        last_join[0] = 47
        pyautogui.press(f'{tecla_elegida[2]}')
    elif boton_data == 143 and last_join[0] != 143: # cuadrado
        last_join[0] = 143
        pyautogui.press(f'{tecla_elegida[1]}')
    elif boton_data == 31 and last_join[0] != 31: # triangulo
            last_join[0] = 31
            pyautogui.press(f'{tecla_elegida[3]}')
    #reasigna el estado de lastjoin
    elif boton_data != last_join[0]:
        last_join[0] = boton_data
        
def elegir_tecla(data):
    if data == "X":
        eleccion = input()
        tecla_elegida.append(eleccion)
        print(eleccion)


def Listar_Dispositivo():
    """
    lista los dispositivos y printea nombre y id del producto
    """
    #falta agregar la opcion de seleccionar, lo hare cuando tenga ui?
    dispositivos = hid.HidDeviceFilter().get_devices()
    dispositivos[4].open()
    datos = dispositivos[4].set_raw_data_handler(handler)
    input()#esto para que no se cierre
    dispositivos[4].close()

for tecla in teclas:
    check = True
    while check:
        print(f"Coloque la tecla {tecla}")
        eleccion = input()
        if len(eleccion) > 1:
            check = True
        else:
            tecla_elegida.append(eleccion)
            check = False
Listar_Dispositivo()
    
