#Escribir un programa que pregunte al usuario por el número de horas 
#trabajadas y el coste por hora. Después debe mostrar por pantalla 
#la paga que le corresponde.
horas_trabajadas= float(input("¿Cuántas horas has trabajado?")) 
paga_por_hora= float(input("¿Cuánto cobras por hora?"))
paga_correspondiente = horas_trabajadas * paga_por_hora
print(paga_correspondiente, end= '€\n')
