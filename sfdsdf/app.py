import funciones as f

contadorvip=0
contadorgaleria=0
contadorcancha=0

rut = input("ingresa rut: ")
while f.validar_rut(rut):
    rut= input("ingresa rut: ")

correo=input("ingresa correo: ")
while not f.validar_correo(correo):
    correo=input("ingresa correo: ")

while True:
    opc = f.menu()

    if opc == "1":
        contadorvip += 1

    elif opc == "2":
        
        contadorgaleria += 1

    elif opc == "3":
        contadorcancha += 1
        
    else:
        print("ingresar nuevamente")

    seguir = input("quiere seguir comprando? (si/no)")
    while seguir != "si" and seguir != "no":
        seguir = input("quiere seguir comprando? (si/no)")

    if seguir == "si":
        continue
    elif seguir == "no":
        break


f.generar_boleta(contadorvip,contadorgaleria,contadorcancha)