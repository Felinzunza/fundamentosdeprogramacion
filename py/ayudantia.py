#Función para verificar si un número es par o impar:
#Crea una función que tome un número entero como argumento 
# y devuelva "Par" si el número es par y "Impar" si el número es impar.


def tiponumero(num):
    
    
    if num % 2 == 0:
        print("numero es par")
    elif num % 2 != 0:
        print("numero es impar")
    else:
        print("no es numero entero")

    return


numero=int(input("agregar numero: "))
tiponumero(numero)

#Función para contar palabras en una cadena:
# Escribe una función que reciba una cadena de texto y devuelva el número de palabras que contiene.

def escadena(palabra):
    
    return palabra
    

contletra=input("agregar palabras: ")

escadena(contletra)
print(f"hay {len(contletra)} letras de la palabra: {contletra}")

#Función para encontrar el número más grande en una lista:
# Crea una función que tome una lista de números como argumento y devuelva el número más grande en la lista.

import random

def largo(rango): 
    eslista =[] 
    rango=int(rango)
    
    for i in range (rango):
        i =random.randint(1, 99)
        eslista.append(i)

    print(eslista)
    print(f"el numero mas grande es {max(eslista)} de la lista")


listrang=int(input("agregar un rango de numeros"))
largo(listrang)
