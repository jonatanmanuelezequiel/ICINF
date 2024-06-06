
contador_de_ingresos=0
dia=1
lista_puntajes=[]
while contador_de_ingresos<15:
    puntajes=0
    print(("día "), dia)
    puntajes=input("puntaje: ")
    lista_puntajes.append(puntajes)
    contador_de_ingresos=contador_de_ingresos+1
    print(contador_de_ingresos)
    dia=dia+1

revision=0
dias_puntaje_mayor_igual_60=[]
dias_puntaje_menos_60=[]

while revision<4:
    revision=revision+1
    for i in lista_puntajes:
        if i>=60:
            dias_puntaje_mayor_igual_60.append(x)
        elif i<60:
            dias_puntaje_menos_60.append(x)
            
dias_2=0
for x in lista_puntajes:
    dias_2=dias_2+1
    if dias_puntaje_mayor_igual_60 in lista_puntajes:
        print("dia", dias_2)
        print("el puntaje fue mayor o igual a 60")
    elif dias_puntaje_menos_60 in lista_puntajes:
        print("dia", dias_2)
        print("el puntaje fue menor a 60")
        
        
    
            