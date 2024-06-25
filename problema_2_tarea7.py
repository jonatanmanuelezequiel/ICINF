palabras = []

print("Ingrese una palabra (presione enter para terminar ingreso): ")

while True:
    palabra = input("Ingrese una palabra (presione enter para terminar ingreso): ")
    if palabra == "":
        break
    palabras.append(palabra)

print("\nCantidad de caracteres 'A' o 'a' en cada palabra:")
for palabra in palabras:
    contador_a = 0
    for letra in palabra:
        if letra == 'A' or letra == 'a':
            contador_a += 1
    print(palabra + ": " + str(contador_a))
