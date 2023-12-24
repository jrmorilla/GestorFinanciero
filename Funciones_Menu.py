import datos
import os

def borrar_pantalla():
    os.system('cls')

def menu_principal():
    print(" Estos son los datos de tus cuentas: ")
    print("\n")
    datos.ver_datos_salarios()
    print("\n")
    print("¿Qué deseas hacer?")
    print("\n")
    print("0. Salir")
    print("1. Ingresar dinero")
    print("2. Notificar un gasto")
    print("3. Crear nueva cuenta")
    print("4. Eliminar cuenta")
    print("5. Crear categoría de gasto")
    print("6. Eliminar categoría de gasto")
    print("7. Transferencia entre dos cuentas")
    print("8. Ver actividad")
    print("\n")
    respuesta = int(input("Selecciona un número: "))
    borrar_pantalla()
    return respuesta