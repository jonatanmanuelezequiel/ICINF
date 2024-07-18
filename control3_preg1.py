#Crear un programa en Python que implemente una función
#“digitos(num)”, que devuelva la cantidad de dígitos que tiene
#un número ingresado por el usuario. Se recomienda procesar el
#número como un String.

def digitos(num):
    cant_digitos=0
    num=str(num)
    for x in num:
        cant_digitos=cant_digitos+1
    return print(f"la cantidad de digitos del numero son {cant_digitos}.")

digitos(343643)