lista_palabras = []
vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"

palabra = input("ingrese palabra para agregar a lista: ")
print("(presione enter para terminar ingreso)")

while palabra != "":
    lista_palabras.append(palabra)
    palabra=input("ingrese palabra para agregar a la lista: ")
    print("(presione enter para terminar ingreso)")

for palabra in lista_palabras:
    v=0
    c=0
    print(palabra)
    for letra in palabra:
        if letra in vocales:
            v=v+1
        if letra in consonantes:
                c=c+1
            
    print("el numero de vocales de la palabra es: ",v)
    print("el numero de consonantes de la palabra es: ",c)
    print(" ")