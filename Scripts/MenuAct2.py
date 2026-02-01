import os
from datetime import datetime
import FuncionesAct2 as funciones

#DIRECTORIO = "./clientes"
Directorio = "/home/arge/Escritorio/Axanet/Directorio"

# Menú principal
def menu():
    os.makedirs(Directorio, exist_ok=True)  
    while True:
        print("\n=== Menú de Gestión de Clientes ===")
        print("Seleccione una opción:")
        print("1) Crear cliente")
        print("2) Agregar servicio")
        print("3) Consultar cliente")
        print("4) Listar clientes")
        print("5) Eliminar cliente")
        print("6) Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            funciones.crear_cliente()
        elif opcion == "2":
            funciones.agregar_servicio()
        elif opcion == "3":
            funciones.consultar_cliente()
        elif opcion == "4":
            funciones.listar_clientes()
        elif opcion == "5":
            funciones.eliminar_cliente()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()