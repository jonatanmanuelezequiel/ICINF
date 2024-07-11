def sumatoria(numero):
    sumatorias=[]
    suma=0
    contador=0
    while contador<numero:
        contador=contador+1
        sumatorias.append(contador)
    for x in sumatorias:
        suma=suma+x
    print(f"La sumatoria de {numero} es: \n")
    for x in sumatorias:
        print(x,"+")
    return print("= ",suma)

sumatoria(50)