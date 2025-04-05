from pywinusb import hid
def handler(datos_raw):
    """
    mostrar info array de botones, place 6 contiene los btns del cuadrado, ciruclo, triangulo y x
    """
    print("Raw data:", datos_raw)
    boton_data = datos_raw[6]
    for i in range(8):  # teoricamente hay 8 botones
        if boton_data & (1 << i):
            print(f"boton {i + 1} presionado")


def Listar_Dispositivo():
    """
    lista los dispositivos y printea nombre y id del producto
    """
    dispositivos = hid.HidDeviceFilter().get_devices()

    for dispositivo in dispositivos:
        if hex(dispositivo.product_id) == "0x6":
            try:
                dispositivo.open()
                print("*************************************")
                print(f"Nombre {dispositivo.product_name}")
                print(f"Id Producto: {hex(dispositivo.product_id)}")
                dispositivo.set_raw_data_handler(handler)
                input("Finalizar..")
                print("************************************")
                print(dispositivo.find_input_reports())
                dispositivo.close() 
            except Exception as e:
                print(f"{e}")
                
            
        else:
            print("no se encontro")

        
Listar_Dispositivo()
