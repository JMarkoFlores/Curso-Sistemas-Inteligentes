'''
Calcular la altura que cae un objeto. Se debe ingresar el tiempo recorrido en segundos.  
H = 0.5 * G * T 2     
G = 9.8 m/seg2
'''

try:
        tiempo = int(input("Ingrese el tiempo recorrido (en seg): "))
        G = 9.8
        H = 0.5 * G * (tiempo ** 2)
        print("Calculando altura")
        print(f"Altura percorrida: {H} metros")
except ValueError:
        print("Ingrese valor numérico")
        print(f"Error: {ValueError}")
        
'''
Consideraciones:
1)Potencia(^): Sintaxis de python es **
'''