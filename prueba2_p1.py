lista_de_notas = []

while True:
    ingreso_notas=(float(input("ingrese nota a la lista (ingrese 0 para terminar ingreso): ")))
    if ingreso_notas==0:
        break
    else:
        lista_de_notas.append(ingreso_notas)
suma_nota=0
division=0
promedio=0
nota_menor_4=0
nota_mayor_igual_4=0
for x in lista_de_notas:
    suma_nota=suma_nota+x
    division=division+1
    if x<4.0:
        nota_menor_4=nota_menor_4+1
    else:
        nota_mayor_igual_4=nota_mayor_igual_4+1
    promedio=suma_nota/division
print("la lista tiene ",division," notas")
print("el promedio de las notas es ",promedio,".")
print(nota_menor_4," nota/s es/son menor/es a 4.")
print(nota_mayor_igual_4," nota/s es/son mayor/es o igual/es a 4.")