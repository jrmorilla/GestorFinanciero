import Funciones_Menu
import ingresar_dinero
import datos
import retirar_dinero
import categorias_gasto
import seleccion
import registro_datos
import saldos_operaciones
import categorias_ingreso
import os
from colorama import Fore, Style

def borrar_pantalla():
    os.system('cls')



while True:

    borrar_pantalla()
    num = Funciones_Menu.menu_principal()

    #----------
    # 0. CANCELAR
    #----------


    if num == 0:
        break


    #----------------
    # 1. INGRESAR DINERO
    #----------------


    elif num == 1:
        cuenta = seleccion.seleccion_saldos()

        borrar_pantalla()

        saldo  = float(input(f"¿Cuánto dinero quieres meter en {cuenta}?: "))

        borrar_pantalla()

        categoria = categorias_ingreso.elegir_categoria_ingreso()
        registro_datos.añadir_ingreso(categoria,saldo)

        borrar_pantalla()

        ingresar_dinero.ingresar_dinero(saldo,cuenta)

        print("\n")
        passs = input("Selecciona enter para continuar")


    #-------------------
    # 2. NOTIFICAR GASTO
    #-------------------



    elif num == 2:
        cuenta = seleccion.seleccion_saldos()

        print("\n")
        print(f"Has seleccionado: {cuenta}")

        borrar_pantalla()

        gasto = float(input("¿Cuánto dinero has gastado?: "))

        borrar_pantalla()

        print("Selecciona una categoría: ")
        print("\n")
        categoria = categorias_gasto.elegir_categoria_gasto()
        retirar_dinero.retirar_dinero(gasto,cuenta)
        registro_datos.añadir_gasto(categoria,gasto)
        print("\n")
        passs = input("Selecciona enter para continuar: ")

    #----------------------
    # 3. CREAR NUEVA CUENTA
    #----------------------

    elif num == 3:
        nombre = input("Escribe el nombre de la cuenta que quieres crear: ")
        saldos_operaciones.añadir_cuenta(nombre)


    #-------------------------
    # 4. ELIMINAR CUENTA
    #-------------------------

    elif num == 4:

        cuenta = seleccion.seleccion_saldos()

        borrar_pantalla()

        if cuenta == 0:
            pass
        else:
            decision = input(f"SEGURO QUE QUIERES BORRAR LA CUENTA {cuenta}? YES/NO: ")
            if decision == "YES":
                saldos_operaciones.eliminar_cuenta(cuenta)
                print("Se ha eliminado la cuenta con éxito")
            else:
                print("Se ha cancelado la eliminación")


    #-----------------------------
    # 5. CREAR CATEGORÍA DE GASTO
    #-----------------------------


    elif num == 5:
        print("Estas son las categorías existentes ahora mismo: ")
        print("\n")

        categorias_gasto.ver_categorias()
        print("\n")
        print("Pulsa 0 para cancelar")
        print("\n")
        nombre = str(input("Introduce el nombre de la categoría de gasto que quieres añadir: "))
        if nombre == "0":
            pass
        else:
            categorias_gasto.crear_categoria(nombre)


    #-------------------------------
    # 6. ELIMINAR CATEGORÍA DE GASTO
    #-------------------------------

    elif num == 6:

        categorias_gasto.eliminar_categoria()

    #------------------------------------
    # 7. Transferencia entre dos cuentas
    #------------------------------------


    elif num == 7:
        datos.ver_datos_salarios()
        print("\n")
        print("Selecciona la cuenta desde la que PARTE el dinero:")
        print("\n")
        cuenta_saliente = seleccion.seleccion_saldos()

        if cuenta_saliente == 0:
            print("La operación se ha cancelado")
        else:

            saldo = float(input(f"Introduce el dinero que quieres transferir desde {cuenta_saliente}: "))

            borrar_pantalla()
            datos.ver_datos_salarios()
            print("\n")

            print(f"Selecciona la cuenta a la que le llegará el dinero ({saldo} euros): ")
            print("\n")

            cuenta_entrante = seleccion.seleccion_saldos()

            if cuenta_entrante == 0:
                borrar_pantalla()
                datos.imprimir_linea_en_color("Se ha cancelado la transferencia", Fore.RED)
                print("\n")
                passs = input("Pulsa Enter para salir")
            else:
                borrar_pantalla()
                retirar_dinero.retirar_dinero(saldo,cuenta_saliente)
                ingresar_dinero.ingresar_dinero(saldo,cuenta_entrante)
                print("\n")
                datos.imprimir_linea_en_color("La transferencia se ha realizado con éxito",Fore.LIGHTBLUE_EX)
                print("\n")
                input("Selecciona Enter para continuar")




    elif num == 8:

        mes = datos.seleccion_mes_gastos()
        datos.ver_datos_registro(mes)
        print("\n")
        input("Pulsa enter para continuar")
        borrar_pantalla()










