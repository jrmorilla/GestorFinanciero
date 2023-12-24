import seleccion
import os

def añadir_cuenta(nombre):

    # Ruta de la carpeta

    nombre_nuevo = f"{nombre}.txt"

    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Saldos'

    # Obtener la lista de nombres de archivos:

    archivos = os.listdir(carpeta)

    if nombre_nuevo not in archivos:
        nuevo_archivo = open(f"C:\\Users\\moril\\GestorFinanciero\\Saldos\\{nombre_nuevo}","w")
        print("La cuenta se ha creado con éxito")

    else:
        print("Esa cuenta ya existe")

def eliminar_cuenta(nombre):

    archivo = f'C:\\Users\\moril\\GestorFinanciero\\Saldos\\{nombre}'
    try:
        os.remove(archivo)
    except:
        print("No se ha podido borrar. Esa cuenta no existe")

