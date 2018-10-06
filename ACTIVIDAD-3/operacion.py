def cambio(dinero,uno,dos,tres,cuatro,cinco,seis,siete,ocho):
    """clase base"""
    if dinero == 0:
        print("0")
    else:
        print("su cambio es:")
        if uno >= 1:
            if uno == 1 : return print(uno, "Billete de 200 pesos")
            if uno>1: return print(uno,"billetes de 200 pesos")
        if dos >= 1:
            if dos==1: return print(dos, "Billete de 100 pesos")
            if dos>1: return print(dos, "Billetes de 100 pesos")
        if tres >= 1:
            if tres==1: return print(tres, "Billete de 50 pesos")
            if tres>1: return print(tres, "Billetes de 50 pesos")
        if cuatro >= 1:
            if cuatro==1: return print(cuatro, "Billete de 20 pesos")
            if cuatro>1: return print(cuatro, "Billetes de 20 pesos")
        if cinco >= 1:
            if cinco==1: return print(cinco, "moneda de 10 pesos")
            if cinco>1: return  print(cinco, "monedas de 10 pesos")
        if seis >= 1:
            if seis==1: return print(seis, "moneda de 5 pesos")
            if seis>1: return print(seis, "monedas de 5 pesos")
        if siete >= 1:
            if siete==1: return print(siete, "moneda de 2 pesos")
            if siete>1: return print(siete, "monedas de 2 pesos")
        if ocho >= 1:
            if ocho==1: return print(ocho, "moneda de 1 peso")
            if ocho>1: return print(ocho, "monedas de 1 peso")