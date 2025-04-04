from pywinusb import hid
def handler(datos_raw):
    print("Raw data:", datos_raw)

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
