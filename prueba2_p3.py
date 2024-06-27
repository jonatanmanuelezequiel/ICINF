capitales_pais= {}
nombres = []

nombre_1=input("ingrese nombre de turista 1: ")
capital_1=input("ingrese capital de procedencia: ")
pais_1=input("ingrese pais: de procedencia: ")
capitales_pais[capital_1]=pais_1

nombre_2=input("ingrese nombre de turista 2: ")
capital_2=input("ingrese capital de procedencia: ")
pais_2=input("ingrese pais de procedencia: ")
capitales_pais[capital_2]=pais_2
nombre_3=input("ingrese nombre de turista 3: ")
capital_3=input("ingrese capital de procedencia: ")
pais_3=input("ingrese pais de procedencia= ")
capitales_pais[capital_3]=pais_3
nombre_4=input("ingrese nombre de turista 4: ")
capital_4=input("ingrese capital de procedencia: ")
pais_4=input("ingrese pais de procedencia: ")
capitales_pais[capital_4]=pais_4
nombre_5=input("ingrese nombre de turista 5: ")
capital_5=input("ingrese capital de procedencia: ")
pais_5=input("ingrese pais de procedencia: ") 
capitales_pais[capital_5]=pais_5

#hasta aqui funciona bien

for x in capitales_pais:
        if capital_1 in x:
            print("el turista con el nombre ",nombre_1," viene de la capital ",capital_1," y su país es " )
            print(capitales_pais[capital_1])
            print("el turista con el nombre ",nombre_2," viene de la capital ",capital_2," y su país es " )
            print(capitales_pais[capital_2])
        elif capital_3 in x:
            print("el turista con el nombre ",nombre_3," viene de la capital ",capital_3," y su país es " )
            print(capitales_pais[capital_3])
        elif capital_4 in x:
            print("el turista con el nombre ",nombre_4," viene de la capital ",capital_4," y su país es " )
            print(capitales_pais[capital_4])
        elif capital_5 in x:
            print("el turista con el nombre ",nombre_5," viene de la capital ",capital_5," y su país es " )
            print(capitales_pais[capital_5])