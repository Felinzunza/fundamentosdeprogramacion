def registro_usuario(lista_usuario):
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    cargo= input("cargo: ")
    sueldo = input("sueldo")
    usuario ={
         "nombre": nombre,
         "apellido": apellido,
         "cargo":cargo,
         "sueldo": sueldo,
         "desc_salud": int(sueldo) * 0.07,
         "desc_afp": int(sueldo)*0.12,
        }
    
    lista_usuario.append(usuario)
    


def lista_usuario(lista_trabajadores):
    for trabajador in lista_trabajadores:
        print(f"{trabajador["nombre"]} {trabajador["apellido"]} " )
        print(f"{trabajador["cargo"]}")
        print(f"{trabajador["sueldo"]}")

def planilla(lista_trabajadores, cargo):
    
    for trabajador in lista_trabajadores:
        if trabajador["cargo"] == cargo: #esto hay que imprimirlo en un arhivo, no en la consola
            print(f"{trabajador["nombre"]} {trabajador["apellido"]} " )
            print(f"{trabajador["cargo"]}")
            print(f"{trabajador["sueldo"]}")
      