import os
from datetime import datetime
import Funcion_Clientes as Clientes
import Funcion_Servicio as Servicio

#DIRECTORIO = "./clientes"
Directorio = "/home/arge/Escritorio/Axanet/Directorio"

# Menú principal
def menu():
    os.makedirs(Directorio, exist_ok=True)  
    while True:
        print("\n=== Menú de Gestión de Clientes ===")
        print("Seleccione una opción:")
        print("1) Crear cliente")
        print("2) Modificar cliente")
        print("3) Eliminar cliente")
        print("4) Consultar cliente")
        print("5) Listar clientes")
        print("6) Agregar servicio")
        print("7) Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            Clientes.crear_cliente()
        elif opcion == "2":
            Clientes.modificar_cliente()
        elif opcion == "3":
            Clientes.eliminar_cliente()
        elif opcion == "4":
            Clientes.consultar_cliente()
        elif opcion == "5":
            Clientes.listar_clientes()
        elif opcion == "6":
            Servicio.agregar_servicio()
        elif opcion == "7":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()