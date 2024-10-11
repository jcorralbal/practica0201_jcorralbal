#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
# tiene un descuento del 60%. Escribir un programa que comience leyendo el
# número de barras vendidas que no son del día. Después el programa debe 
# mostrar el precio habitual de una barra de pan, el descuento que se le hace 
# por no ser fresca y la ganancia final total.


precio_barra = 3.49
descuento = 0.60
barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))
precio_con_descuento = precio_barra * (1 - descuento)
ganancia_total = barras_no_frescas * precio_con_descuento
print(f"Precio habitual de una barra de pan: {precio_barra}€")
print(f"Descuento por no ser fresca: {descuento * 100}%")
print(f"Ganancia final total: {ganancia_total:.2f}€")
