
ventana = []
pasillo = []

for i in range(1, 21):
    if i % 2 == 0:
        pasillo.append(i)
    else:
        ventana.append(i)

opc=None
opc1=None
opc2=None
opc3=None
while opc !="4":

    print("menu principal")
    print("1. pagar")
    print("2. seleccionar boleto")
    print("3. resumen")
    print("4. salir")
    opc=input("elegir opcion ")
    
    if opc== "1":
        while opc1 !=  "s":
            print("cual es su destino?")
            print("1. Florida")
            print("2. Quillón")
            destino=int(input())
            if destino == 1:
                print("destino: florida")
            elif destino == 2:
                print("destino: quillon")

            
    elif opc=="2":
        while opc2 != "s":
            print("Asientos actualizados:")
            print(f"ventana = {ventana}")
            print(f"pasillo = {pasillo}")
            asiento=int(input("agregar asiento: "))

            if asiento % 2 == 0:
                if asiento in pasillo:
                    indice = pasillo.index(asiento)
                    pasillo[indice] = 'x'
                    print("Elegiste pasillo")
                    conteopasillo=conteopasillo+1
                else:
                    print("El asiento no está disponible en pasillo.")
            else:
                if asiento in ventana:
                    indice = ventana.index(asiento)
                    ventana[indice] = 'x'
                    print("Elegiste ventana")
                    conteoventana=conteoventana+1
                else:
                    print("El asiento no está disponible en ventana.")
            print()
            print("¿deseas volver?")
            print("s. si")
            print("n. no")
            opc2=input()
            
            
    elif opc=="3":
        
        print("resumen...")

    elif opc == "4":
        print("salir")
    
    else:
        print("opcion equivocada")
        


print("sali del bucle")