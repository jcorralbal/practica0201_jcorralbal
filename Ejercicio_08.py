#Escribir un programa que pida al usuario dos números enteros y muestre 
#por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde 
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el 
#cociente y el resto de la división entera respectivamente.

print("A continuación introduzca un dividendo y un divisor")
while True:
    try: 
        n = int(input("Introduzca su dividendo: "))
        m = int(input("Introduzca su divisor: "))
        if m == 0:
            print("No puedes dividir entre cero")
            continue
        else:
            c = n // m
            r = n % m       
            print(
                "El número {} entre {} da un cociente {} y un resto {}"
                .format(n, m, c, r)
            )
            break
    except ValueError:
        print("Error. Introduzca un valor válido") 
