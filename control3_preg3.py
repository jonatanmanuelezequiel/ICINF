def potencia(num,exp):
    global cont1,multiplicacion
    producto=num
    multiplicacion=producto*producto
    multiplicacion=multiplicacion*num
    cont=0
    cont1=cont+1
    if cont<=exp:
        return print(f"el resultado de la potencia del numero {num} con exponente {exp} es {multiplicacion}.")
    potencia(num,exp)
    
potencia(4,5)