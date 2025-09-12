'''
3)Leer un número entero que represente días y determinar a cuanto equivale en años, 
meses y días (Asumir que todos los años tienen 360 días y que todos los meses tienen 30 
días).
'''

diasTotales = int(input('Ingrese la cantidad de dias: '))
anyos = int(diasTotales/360)
meses = int((diasTotales % 360)/30)
dias = (diasTotales % 360) % 30
print(f"Cantidad de años: {anyos}")
print(f"Cantidad de meses: {meses}")
print(f"Cantidad de dias: {dias}")

'''
Consideraciones:
1)Utilizar // (division entera) en vez de poner int(division)
2)La sintaxis de los conectores lógicos "&&", "||" y "not" en python: "and", "or", "not" 
'''