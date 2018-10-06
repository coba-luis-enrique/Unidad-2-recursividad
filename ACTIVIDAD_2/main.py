#Programa para saber si una palabra es un palindromo.
from  operacion import *

print("Binario: ")
print("Selecciona una opción: ")
print("\t1 - Inicio")
print("\t2 - Salida")
# solicituamos una opción al usuario
opcionMenu = input("\ninserte de una opcion>> ")

if opcionMenu=="1":
    numero = int(input("Ingresa un numero: "))
    print(binario(numero))
elif opcionMenu=="2":
    print("Has salido....")
else:
    print("opcion incorrects...")


