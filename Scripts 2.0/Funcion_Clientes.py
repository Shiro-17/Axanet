import os
from datetime import datetime

#Direccion de la carpeta
Directorio = "/home/arge/Escritorio/Axanet/Directorio"

# Diccionario (tabla hash) para asociar nombre → archivo
clientes = {}

# Crear cliente
def crear_cliente():
    nombre = input("Ingrese nombre del cliente: ").title()

    ruta = os.path.join(Directorio, nombre)

    if os.path.exists(ruta):
        print(f"El cliente {nombre} ya fue creado anteriormente.")
        return

    os.makedirs(ruta, exist_ok=True)

    archivo_cliente = os.path.join(ruta, "archivo_cliente.txt")
    with open(archivo_cliente, "w") as f:
        f.write(f"Cliente: {nombre}\n")

    clientes[nombre] = archivo_cliente

    descripcion = input("Ingrese descripción del servicio: ")
    direccion = input("Ingrese dirección del servicio: ")
    fecha = datetime.now().strftime("%Y-%m-%d")

    archivo_servicios = os.path.join(Directorio, nombre, "servicios.txt")
    with open(archivo_servicios, "a") as f:
        f.write(f"Servicio: {descripcion} | Dirección: {direccion} | Fecha: {fecha}\n")


    print(f"Cliente y datos creados a nombre de: {nombre} ")

# Modificar cliente
def modificar_cliente():
    nombre_actual = input("Ingrese el nombre actual del cliente: ").title()
    ruta_actual = os.path.join(Directorio, nombre_actual)

    if not os.path.exists(ruta_actual):
        print(f"El cliente {nombre_actual} no existe.")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ").title()
    ruta_nueva = os.path.join(Directorio, nuevo_nombre)

    # Verificar que el nuevo nombre no exista ya
    if os.path.exists(ruta_nueva):
        print(f"Ya existe un cliente con el nombre {nuevo_nombre}.")
        return

    # Renombrar la carpeta
    os.rename(ruta_actual, ruta_nueva)

    # Actualizar archivo_cliente.txt con el nuevo nombre
    archivo_cliente = os.path.join(ruta_nueva, "archivo_cliente.txt")
    if os.path.exists(archivo_cliente):
        with open(archivo_cliente, "w") as f:
            f.write(f"Cliente: {nuevo_nombre}\n")

    # Actualizar el diccionario en memoria
    clientes.pop(nombre_actual, None)
    clientes[nuevo_nombre] = archivo_cliente

    print(f"Cliente {nombre_actual} modificado a {nuevo_nombre}.")

# Consultar cliente
def consultar_cliente():
    nombre = input("Ingrese nombre del cliente: ").title()
    ruta = os.path.join(Directorio, nombre)

    if not os.path.exists(ruta):
        print("Cliente no encontrado.")
        return

    archivo_cliente = os.path.join(ruta, "archivo_cliente.txt")
    archivo_servicios = os.path.join(ruta, "servicios.txt")

    if os.path.exists(archivo_cliente):
        with open(archivo_cliente, "r") as f:
            print(f.read())

    print("Servicios:")
    if os.path.exists(archivo_servicios):
        with open(archivo_servicios, "r") as f:
            print(f.read())
    else:
        print("No hay servicios registrados.")

# Eliminar cliente
def eliminar_cliente():
    nombre = input("Ingrese nombre del cliente: ").title()
    ruta = os.path.join(Directorio, nombre)

    if not os.path.exists(ruta):
        print(f"El cliente {nombre} no existe.")
        return

    for archivo in os.listdir(ruta):
        os.remove(os.path.join(ruta, archivo))

    os.rmdir(ruta)

    clientes.pop(nombre, None)

    print(f"Cliente {nombre} eliminado correctamente.")

# Listar clientes
def listar_clientes():
    if os.path.exists(Directorio):
        print("Clientes registrados:")
        for i, cliente in enumerate(os.listdir(Directorio), start=1):
            print(f"{i}. {cliente}")
    else:
        print("No hay clientes registrados.")
