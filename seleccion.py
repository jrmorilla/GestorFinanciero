import os

def seleccion_saldos():

    # Ruta de la carpeta

    carpeta = 'C:\\Users\\moril\\GestorFinanciero\\Saldos'

    # Obtener la lista de nombres de archivos:

    archivos = os.listdir(carpeta)

    nums = []
    for num in range(1,len(archivos)+1):
        nums.append(num)
    zipeados = list(zip(nums,archivos))

    print("Estas son todas tus cuentas:")
    print("\n")
    print("Pulsa 0 para cancelar")
    print("\n")
    for num, saldo in zipeados:
        print(num, saldo)
    print("\n")
    seleccion = int(input("Selecciona una cuenta: "))
    if seleccion == 0:
        return 0
    else:
        return zipeados[seleccion-1][1]





