from pywinusb import hid
import pyautogui
last_join = [None]
def handler(datos_raw):
    """
    mostrar info array de botones, place 6 contiene los btns del cuadrado, ciruclo, triangulo y x
    """
    
    if datos_raw[6] > 15 and datos_raw[3] < 115 or datos_raw[3] > 130 : #esto para controlar el spam de mi joystick no necesario
        print("Raw data:", datos_raw)
    boton_data = datos_raw[6]
    if boton_data == 79 and last_join[0] != 79:
        last_join[0] = 79
        pyautogui.keyDown('x')
    #reasigna el estado de lastjoin
    elif boton_data != last_join[0]:
        last_join[0] = boton_data
        pyautogui.keyUp('x')



def Listar_Dispositivo():
    """
    lista los dispositivos y printea nombre y id del producto
    """
    dispositivos = hid.HidDeviceFilter().get_devices()
    dispositivos[4].open()
    datos = dispositivos[4].set_raw_data_handler(handler)
    input()#esto para que no se cierre
    dispositivos[4].close()

        
Listar_Dispositivo()
