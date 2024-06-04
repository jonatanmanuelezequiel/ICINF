lista_palabras = []
opcion = 0

while opcion != 7:
    print("1. Para ingresar un elemento a la lista.")
    print("2. Para modificar un elemento de la lista según el índice.")
    print("3. Para eliminar un elemento de la lista según el índice.")
    print("4. Para eliminar el último elemento de la lista.")
    print("5. Para buscar un elemento en la lista.")
    print("6. Para mostrar todos los elementos de la lista.")
    print("7. Para salir.")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        palabra = input("Ingrese palabra para agregar a la lista (presione enter para terminar ingreso): ")
        lista_palabras.append(palabra)
        
    elif opcion == 2:
        modificar_elemento = int(input("Ingrese índice de elemento a modificar: "))
        if modificar_elemento < len(lista_palabras):
            modificacion = input("Ingrese nuevo elemento: ")
            lista_palabras[modificar_elemento] = modificacion
        else:
            print("El índice está fuera de rango.")
        
    elif opcion == 3:
        eliminar_elemento = int(input("Ingrese índice de elemento a eliminar: "))
        if eliminar_elemento < len(lista_palabras):
            lista_palabras.pop(eliminar_elemento)
        else:
            print("El índice está fuera de rango.")
        
    elif opcion == 4:
        if lista_palabras:
            lista_palabras.pop()
            print("Último elemento de la lista eliminado.")
        else:
            print("La lista está vacía.")
        
    elif opcion == 5:
        buscar_elemento = input("Ingrese dato a buscar en la lista: ")
        if buscar_elemento in lista_palabras:
            print("El elemento", buscar_elemento, "está en la lista.")
        else:
            print("El elemento", buscar_elemento, "no está en la lista.")
        
    elif opcion == 6:
        print("Elementos de la lista:")
        print(lista_palabras)
        
    elif opcion == 7:
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida.")

print("Bucle finalizado.")