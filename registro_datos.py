import datetime
import os


def obtener_cuaterna():

    # Obtener la fecha actual en el formato deseado (DD, MM, AA)

    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d,%m,%y")

    # Convertir el número del mes a su nombre completo

    nombre_mes = fecha_actual.strftime("%B")

    # Generar la terna (día, mes, año)

    terna = (fecha_actual.day, nombre_mes, fecha_actual.month, fecha_actual.year)
    return terna




# Formato de archivos (en carpeta gastos_total): MM-AA
def crear_txt_mes():
    cuaterna = obtener_cuaterna()
    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total'
    archivos = os.listdir(carpeta)
    mes = cuaterna[1]
    año = cuaterna[3]
    nombre = f"{mes}-{año}.txt"

    if nombre in archivos:
        pass
    else:
        ruta_completa = f'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total\\{nombre}'
        archivo = open(ruta_completa,"w")



def añadir_gasto(categoria, cantidad):

    crear_txt_mes()
    cuaterna = obtener_cuaterna()
    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total'
    dia = cuaterna[0]
    mes = cuaterna[1]
    año = cuaterna[3]
    nombre = f"{mes}-{año}.txt"
    ruta_final = f'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total\\{nombre}'
    archivo = open(ruta_final,"a")
    fecha = f"{dia}/{mes}/{año}"
    contenido = f'- {fecha } ---- { cantidad} euros ---- {categoria}'
    archivo.write(contenido + "\n")
    archivo.close()




def añadir_ingreso(categoria, cantidad):
    crear_txt_mes()
    cuaterna = obtener_cuaterna()
    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total'
    dia = cuaterna[0]
    mes = cuaterna[1]
    año = cuaterna[3]
    nombre = f"{mes}-{año}.txt"
    ruta_final = f'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total\\{nombre}'
    archivo = open(ruta_final, "a")
    fecha = f"{dia}/{mes}/{año}"
    contenido = f'+ {fecha} ---- {cantidad} euros ---- {categoria}'
    archivo.write(contenido + "\n")
    archivo.close()

