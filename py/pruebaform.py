#registrar trabajador
import registro

lista = []
diccionario={}

while True:
    print("menu")
    print("1. registrar trabajador")
    print("2. lista de todos los trabajadores")
    print("3. imprimir planilla de sueldos")
    print("4 salir del programa")
    opcion = input("opcion: ")

    if opcion == "1":
        registro.registro_usuario(lista)
        print()
    elif opcion == "2":
        registro.lista_usuario(lista)
    elif opcion == "3":
        cargo = input("cargo:" )
        registro.planilla(lista)
        print()
    elif opcion == "4":
        print("saliendo")
        break

    else:
        print("")
    