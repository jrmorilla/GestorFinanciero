def retirar_dinero(cantidad,cuenta):
    archivo = open("C:\\Users\\moril\\GestorFinanciero\\Saldos\\"+cuenta, "r")
    contenido = archivo.read().strip()
    archivo.close()

    # Teniendo en cuenta que el archivo puede no estar vacío hacemos lo siguiente:

    if contenido:
        dinero_actual = float(contenido)
    else:
        dinero_actual = 0.0

    # No podemos tener dinero negativo, así que hay que hay que contemplar ese caso:

    if cantidad > dinero_actual:
        print(f"Tu cuenta {cuenta} está en números rojos")
        print("\n")

        nuevo_total = round(dinero_actual - cantidad)

        # Abrimos el archivo en modo de escritura para actualizarlo

        archivo = open("C:\\Users\\moril\\GestorFinanciero\\Saldos\\"+ cuenta, "w")

        # Escribimos el nuevo contenido con la cantidad de dinero actualizada

        archivo.write(str(nuevo_total))

        print(f"El dinero ha sido actualizado. Dispone de {nuevo_total} euros en su cuenta {cuenta}")



    else:
        nuevo_total = round(dinero_actual - cantidad)

        # Abrimos el archivo en modo de escritura para actualizarlo

        archivo = open("C:\\Users\\moril\\GestorFinanciero\\Saldos\\"+cuenta, "w")

        # Escribimos el nuevo contenido con la cantidad de dinero actualizada

        archivo.write(str(nuevo_total))

        print(f"El dinero ha sido actualizado. Dispone de {nuevo_total} euros en su cuenta {cuenta}")



