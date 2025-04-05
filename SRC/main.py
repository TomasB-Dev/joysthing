from pywinusb import hid
import pyautogui
last_join = [""] * 2
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
        0, #up
        11, #derecha
        ]
tecla_elegida = [""] * 20 #momentaneo
def handler(datos_raw):
    """
    mostrar info array de botones, place 6 contiene los btns del cuadrado, ciruclo, triangulo y x
    """
    if datos_raw[6] > 15 and datos_raw[3] < 115 or datos_raw[3] > 130 : #esto para controlar el spam de mi joystick no necesario
        print("Raw data:", datos_raw)
    boton_data = datos_raw[6]
    gatillos_btn = datos_raw[7]
    # btn principales xov
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
    elif boton_data == 0 and last_join[0] != 0: # up
            last_join[0] = 0
            pyautogui.press(f'{tecla_elegida[10]}')
    elif boton_data == 2 and last_join[0] != 2: # up
            last_join[0] = 2
            pyautogui.press(f'{tecla_elegida[11]}')
    #reasigna el estado de lastjoin
    elif boton_data != last_join[0]:
        last_join[0] = boton_data
    #GATILLOS

    if gatillos_btn == 1 and last_join[1] != 1:
        last_join[1] = 1
        pyautogui.press(f'{tecla_elegida[4]}')
    if gatillos_btn == 2 and last_join[1] != 2:
        last_join[1] = 2
        pyautogui.press(f'{tecla_elegida[5]}')
    if gatillos_btn == 4 and last_join[1] != 4:
        last_join[1] = 4
        pyautogui.press(f'{tecla_elegida[6]}')
    if gatillos_btn == 8 and last_join[1] != 8:
        last_join[1] = 8
        pyautogui.press(f'{tecla_elegida[7]}')
    elif gatillos_btn != last_join[1]:
        last_join[1] = gatillos_btn
def elegir_tecla(ubicacion,data):
    """selecciona la tecla elegida y la guarda en el espacio correspondiente"""
    tecla_elegida[ubicacion] = data
    print(f"***{tecla_elegida[ubicacion]}***")



def Listar_Dispositivo():
    """
    lista los dispositivos y printea nombre y id del producto
    """
    #falta agregar la opcion de seleccionar, lo hare cuando tenga ui?
    dispositivos = hid.HidDeviceFilter().get_devices()
    dispositivos[4].open()
    datos = dispositivos[4].set_raw_data_handler(handler)
    input()
    dispositivos[4].close()
