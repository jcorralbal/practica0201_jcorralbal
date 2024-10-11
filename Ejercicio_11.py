#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4%
#de interés al año. Estos ahorros debido a intereses, que no se cobran hasta
#finales de año, se te añaden al balance final de tu cuenta de ahorros.
#Escribir un programa que comience leyendo la cantidad de dinero depositada
#en la cuenta de ahorros, introducida por el usuario. Después el programa 
# debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
# segundo y tercer años. Redondear cada cantidad a dos decimales

cantidad_inicial = float(input("Introduce la cantidad depositada en la cuenta de ahorros: "))
tasa_interes = 0.04
balance_1 = cantidad_inicial * (1 + tasa_interes)
balance_2 = balance_1 * (1 + tasa_interes)
balance_3 = balance_2 * (1 + tasa_interes)
balance_1 = round(balance_1, 2)
balance_2 = round(balance_2, 2)
balance_3 = round(balance_3, 2)
print(f"Balance después del primer año: {balance_1}")
print(f"Balance después del segundo año: {balance_2}")
print(f"Balance después del tercer año: {balance_3}")