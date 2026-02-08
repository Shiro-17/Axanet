import os
from datetime import datetime

#Direccion de la carpeta
Directorio = "/home/arge/Escritorio/Axanet/Directorio"

# Diccionario (tabla hash) para asociar nombre → archivo
clientes = {}

# Agregar servicio
def agregar_servicio():
    nombre = input("Ingrese nombre del cliente: ").title()
    ruta_cliente = os.path.join(Directorio, nombre)
    
    if not os.path.exists(ruta_cliente):
        print("Cliente no encontrado en el sistema.")
        return

    descripcion = input("Ingrese descripción del servicio: ")
    direccion = input("Ingrese dirección del servicio: ")
    fecha = datetime.now().strftime("%Y-%m-%d")

    archivo_servicios = os.path.join(Directorio, nombre, "servicios.txt")
    with open(archivo_servicios, "a") as f:
        f.write(f"Servicio: {descripcion} | Dirección: {direccion} | Fecha: {fecha}\n")

    print(f"Servicio agregado al cliente {nombre}")

