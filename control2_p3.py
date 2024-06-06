
lista=[]
lista_de_caractares=[]
while True:
    palabra=input("ingrese palabra a la lista: ")
    print("(para terminar ingreso presione enter)")
    lista.append(palabra)
    if palabra=="":
        break
lista_palabras=[]
for x in lista:
    contador=0
    for i in x:
        contador=contador+1
    lista_de_caractares.append(contador)
lista_de_caractares.sort
mayor_cant_car=lista_de_caractares[0]
print(("la mayor cantidad de caracteres entre las palabras son: "), mayor_cant_car)