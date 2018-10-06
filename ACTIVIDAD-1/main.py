#Programa para saber si una palabra es un palindromo.
from  operacion import *

print("Palindromo: ")
print("Selecciona una opción: ")
print("\t1 - Inicio")
print("\t2 - Salida")
# solicituamos una opción al usuario
opcionMenu = input("\ninserte de una opcion>> ")

if opcionMenu=="1":
    palabra = input("Ingresa el palindromo: ")
    prototipo = operaciones(palabra)
    if prototipo.palindromo() == True:
        print(palabra,"es palindromo")
    else:
        print(palabra," no es palindromo")

elif opcionMenu=="2":
    print("Has salido....")
else:
    print("opcion incorrects...")