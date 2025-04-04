from pywinusb import hid
#no significa que todos sean joysticks
dispositivos = hid.HidDeviceFilter().get_devices()

for dispositivo in dispositivos:
    dispositivo.open()
    print(f"Nombre {dispositivo.product_name}")
    print(f"Id Producto: {hex(dispositivo.product_id)}")
    dispositivo.close()
