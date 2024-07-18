#Crear un programa en Python que implemente una función
#“es_binario(var)”, que permita determinar si un string está
#compuesto por una expresión binaria o no, es decir, que
#contenga solo unos y ceros. La función debe devolver un True,
#si es que es una expresión binaria, o un False, en caso
#contrario. NO DEBE UTILIZAR FUNCIONES PREDEFINIDAS DE PYTHON O
#LIBRERÍAS para determinar si es binario.
def es_binario(var):
    binario=0
    var=str(var)
    for x in var:
        if x!="0":
            if x!="1":
                binario=0
                return (print(False))
        else:
            binario=binario+1
    if binario!=0:
        return print(True)

es_binario(10101010110101010)
es_binario(73479359489)