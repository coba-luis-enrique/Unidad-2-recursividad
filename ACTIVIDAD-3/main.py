from operacion import *

print("Programa que determina el saldo de cambio ")
costo = int(input("saldo pagado:"))
compra=int(input("saldo de la compra: "))

dinero=costo-compra


uno = dinero // 200
restouno = dinero % 200
dos = restouno // 100
restodos = restouno % 100
tres = restodos // 50
restotres = restodos % 50
cuatro = restotres // 20
restocuatro = restotres % 20
cinco = restocuatro // 10
restocinco = restocuatro % 10
seis = restocinco // 5
restoseis = restocinco % 5
siete=restoseis//2
restosiete=restoseis % 2
ocho=restosiete//1
ocho=restosiete % 2

cambio(dinero,uno,dos,tres,cuatro,cinco,seis,siete,ocho)

