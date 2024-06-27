productos_y_precios = {}
valor_dolar = 950.0
contador=0
formula=1
while contador<=9:
    producto=(input("ingrese producto: "))
    precio=float(input("ingrese precio de producto: "))
    productos_y_precios[producto]=precio
    print(productos_y_precios)
    contador=contador+1                                  #hasta aqui funciona bien

for x in productos_y_precios:
    conversion_precio=[x]*formula
    conversion_precio=conversion_precio/valor_dolar
    productos_y_precios[x]==conversion_precio

print("lista de precios con precios convertidos a dolares: ")
print(productos_y_precios)
