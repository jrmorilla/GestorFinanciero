import os
import colorama
from colorama import Fore, Style
import os

def borrar_pantalla():
    os.system('cls')


def ver_datos_salarios():

    # Ruta de la carpeta

    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Saldos'

    # Obtener la lista de nombres de archivos:

    archivos = os.listdir(carpeta)

    for archivo in archivos:
        indice_punto = archivo.rfind('.')
        archivo_nuevo = archivo[:indice_punto]
        arch = open(carpeta + '/' + archivo,'r')
        contenido = arch.read().strip()

        if contenido:
            imprimir_linea_en_color(f"En la cuenta {archivo_nuevo} hay " + contenido + " euros",Fore.BLUE)
        else:
            imprimir_linea_en_color(f"En la cuenta {archivo_nuevo} hay " + "0" + " euros", Fore.BLUE)




def seleccion_mes_gastos():

    # Ruta de la carpeta

    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total'

    # Obtener la lista de nombres de archivos:

    archivos = os.listdir(carpeta)

    nums = []
    for num in range(1,len(archivos)+1):
        nums.append(num)
    zipeados = list(zip(nums,archivos))


    for num, saldo in zipeados:
        print(num, saldo)
    print("\n")
    seleccion = int(input("Selecciona una cuenta: "))
    return zipeados[seleccion-1][1]



# Función para imprimir una línea en el color especificado
def imprimir_linea_en_color(linea, color):
    print(color + linea.strip() + Style.RESET_ALL)


# Nombre del archivo de texto
nombre_archivo = "archivo.txt"

# Inicializar colorama para funcionar en la consola de Windows
colorama.init()


def ver_datos_registro(arch):
    carpeta = f'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total\\{arch}'
    archivo = open(carpeta, "r")
    print("\n")
    for linea in archivo:

        primer_caracter = linea.strip()[0]

        if primer_caracter == "+":
            imprimir_linea_en_color(linea, Fore.GREEN)
        elif primer_caracter == "-":
            imprimir_linea_en_color(linea, Fore.RED)

    dupla = gastos_ingresos_totales(arch)
    ahorro_total = dupla[1] - dupla[0]
    print("\n")
    imprimir_linea_en_color("Ingresos Totales: " + str(dupla[1]), Fore.GREEN)
    imprimir_linea_en_color("Gastos Totales: " + str(dupla[0]), Fore.RED)
    imprimir_linea_en_color(f"Ahorro Total:  {ahorro_total}", Fore.LIGHTBLUE_EX)



def coger_dinero_archivo(linea):
    palabras = linea.split()
    dinero = float(palabras[3])
    return dinero


def gastos_ingresos_totales(arch):
    carpeta = f'C:\\Users\\moril\\GestorFinanciero\\Registros_Gastos\\gastos_total\\{arch}'
    archivo = open(carpeta,"r")

    ingresos = 0
    gastos = 0

    for linea in archivo:
        if linea[0] == "-":
            gastos = gastos + coger_dinero_archivo(linea)
        else:
            ingresos = ingresos + coger_dinero_archivo(linea)
    return (gastos,ingresos)




# print(gastos_ingresos_totales("July-2023.txt"))