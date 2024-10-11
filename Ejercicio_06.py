#Escribir un programa que lea un entero positivo, ,
# introducido por el usuario y después muestre en pantalla
# la suma de todos los enteros desde 1 hasta . 
# La suma de los  primeros enteros positivos puede ser 
# calculada de la siguiente forma: suma = (n * (n + 1)) / 2

while True:
    try:
        n = int(input("Por favor, introduzca un número entero"))
        if n >= 0:
            break
        else: 
            print("El número introducido no es válido")
    except: ValueError
suma = (n * (n + 1)) / 2
print("la suma de todos los enteros desde 1 es:", int(suma))
