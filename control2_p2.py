lista_palabras=[]
lista_a=("a")
nombre=input("ingrese nombre a la lista:")
lista_palabras.append(nombre)
contador=1
while contador<8:
    print("para terminar ingreso presione enter")
    nombre=input("ingrese nombre a la lista:")
    lista_palabras.append(nombre)
    contador=contador+1

lista_con_nombres_a=[]
for x in lista_palabras:
    lista_de_nombre=[]
    for i in x:
        lista_de_nombre.append(i)
    if lista_de_nombre(-1)=="a":
        lista_con_nombres_a.append(x)

print(lista_con_nombres_a)
