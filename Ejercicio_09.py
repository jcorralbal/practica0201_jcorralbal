#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el 
#capital obtenido en la inversión

print("Calcula el capital obtenido en una inversion")
inversion = float(input("Introduzca la cantidad a invertir en euros: "))
interes_anual = float(input("Introduzca el interes anual (en porcentaje): "))
años = int(input("Introduzca el número de años de la inversión: "))
interes_anual_para_calcular = interes_anual / 100
capital_obtenido = inversion * (1 + interes_anual_para_calcular) ** años
print(f"El capital obtenido en la inversión es: {capital_obtenido:.2f} euros")
