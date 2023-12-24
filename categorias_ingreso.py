def elegir_categoria_ingreso():

    palabras = []

    # Abrimos archivo en solo lectura
    # 'C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_ingreso.txt'
    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_ingresos.txt',"r")

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
        seleccion_tipo_ingreso = zipeado[seleccion-1][1]
    return seleccion_tipo_ingreso




def ver_categorias_gasto():

    palabras = []

    # Abrimos archivo en solo lectura

    archivo = open('C:\\Users\\moril\\GestorFinanciero\\Categorias\\tipos_de_ingresos.txt', "r")

    # Leemos cada línea del archivo

    for linea in archivo:
        # Eliminamos espacios en blanco al principio y al final de la línea:

        palabra = linea.strip()

        palabras.append(palabra)

    archivo.close()

    for palabra in palabras:
        print(palabra)

