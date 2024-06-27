capitales_pais= {'santiago':'Chile','brasilia':'Brasil','tokyo':'Japon','seul':'Corea','canberra':'Australia'}

datos_turistas={}
nombre_1=input("ingrese nombre de turista 1: ")
capital_1=input("(capitales: santiago, brasilia, tokyo, seul, canberra)\n ingrese capital de procedencia: ")
datos_turistas[nombre_1]=capital_1
nombre_2=input("ingrese nombre de turista 2: ")
capital_2=input("(capitales: santiago, brasilia, tokyo, seul, canberra)\n ingrese capital de procedencia: ")
datos_turistas[nombre_2]=capital_2
nombre_3=input("ingrese nombre de turista 3: ")
capital_3=input("(capitales: santiago, brasilia, tokyo, seul, canberra)\n ingrese capital de procedencia: ")
datos_turistas[nombre_3]=capital_3
nombre_4=input("ingrese nombre de turista 4: ")
capital_4=input("(capitales: santiago, brasilia, tokyo, seul, canberra)\n ingrese capital de procedencia: ")
datos_turistas[nombre_4]=capital_4
nombre_5=input("ingrese nombre de turista 5: ")
capital_5=input("(capitales: santiago, brasilia, tokyo, seul, canberra)\n ingrese capital de procedencia: ")
datos_turistas[nombre_5]=capital_5
      #hasta aqui funciona bien
for x in datos_turistas:
        if capital_1 in x:
            print("el turista con el nombre ",nombre_1," viene de la capital ",capital_1," y su país es " )
            (print(datos_turistas[capital_1]))
        elif capital_2 in x:
            print("el turista con el nombre ",nombre_2," viene de la capital ",capital_2," y su país es " )
            (print(datos_turistas[capital_2]))
        elif capital_3 in x:
            print("el turista con el nombre ",nombre_3," viene de la capital ",capital_3," y su país es " )
            (print(datos_turistas[capital_3]))
        elif capital_4 in x:
            print("el turista con el nombre ",nombre_4," viene de la capital ",capital_4," y su país es " )
            (print(datos_turistas[capital_4]))
        elif capital_5 in x:
            print("el turista con el nombre ",nombre_5," viene de la capital ",capital_5," y su país es " )
            (print(datos_turistas[capital_5]))