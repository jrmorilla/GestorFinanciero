def elegir_categoria_gasto():

    palabras = []

    # Abrimos archivo en solo lectura

    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto'
    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto.txt',"r")

    # Leemos cada línea del archivo

    for linea in archivo:

        #Eliminamos espacios en blanco al principio y al final de la línea:

        palabra = linea.strip()

        palabras.append(palabra)

    archivo.close()

    long_palabras = len(palabras)

    numeros = []

    # Para que la elección del tipo de gasto sea más amena, lo vamos a hacer mediante números

    for i in range (1,long_palabras+1):
        numeros.append(i)
    zipeado = list(zip(numeros,palabras))

    print("0 Cancelar")
    for clave,valor in zipeado:
        print(clave,valor)
    print("\n")
    seleccion = int(input("Elige el número de la categoría que quieras seleccionar: "))

    if seleccion == 0:
        return "Has cancelado la operación"
    else:
        seleccion_tipo_gasto = zipeado[seleccion-1][1]
    return seleccion_tipo_gasto


def crear_categoria(nombre):

    palabras = []

    # Abrimos el archivo en modo lectura

    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto.txt',"r")

    # Leemos cada línea del archivo

    for linea in archivo:
        # Eliminamos espacios en blanco al principio y al final de la línea:

        palabra = linea.strip()

        palabras.append(palabra)

    archivo.close()

    if nombre not in palabras:


        # Ahora metemos nuestra nueva categoría en la lista de palabras:

        palabras.append(nombre)

        # Ahora sustituimos las palabras del archivo por las palabras de la lista:

        archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto.txt',"w")
        for elemento in palabras:
            archivo.write(elemento + "\n")
        archivo.close()

        print(f"Has creado la categoría {nombre}!")

    else:
        print("Esta categoría de gasto ya existe")

def eliminar_categoria():
    palabras = []

    # Abrimos archivo en solo lectura

    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto.txt', "r")

    # Leemos cada línea del archivo

    for linea in archivo:
        # Eliminamos espacios en blanco al principio y al final de la línea:

        palabra = linea.strip()

        palabras.append(palabra)

    archivo.close()

    long_palabras = len(palabras)

    numeros = []

    # Para que la elección del tipo de gasto sea más amena, lo vamos a hacer mediante números

    for i in range(1, long_palabras + 1):
        numeros.append(i)
    zipeado = list(zip(numeros, palabras))

    print("0 Cancelar")
    for clave, valor in zipeado:
        print(clave, valor)

    print("\n")
    seleccion = int(input("Elige el número de la categoría que quieras ELIMINAR: "))

    if seleccion == 0:
        return "Has cancelado la operación"
    else:
        categoria = palabras[seleccion-1]
        palabras.pop(seleccion-1)

    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto.txt', "w")
    for elemento in palabras:
        archivo.write(elemento + "\n")
    archivo.close()


    print(f"Has eliminado la categoría {categoria} de la lista.")

def ver_categorias():

    palabras = []

    # Abrimos archivo en solo lectura

    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_gasto.txt', "r")

    # Leemos cada línea del archivo

    for linea in archivo:
        # Eliminamos espacios en blanco al principio y al final de la línea:

        palabra = linea.strip()

        palabras.append(palabra)

    archivo.close()

    for palabra in palabras:
        print(palabra)

