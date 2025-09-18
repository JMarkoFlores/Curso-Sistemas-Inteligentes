'''
5) La distancia entre dos puntos (x1, y1) y (x2, y2) de un plano se puede obtener sacando la raíz cuadrada de la expresión (x2 – x1)2 + (y2 – y1)2. Escribir un programa que, dados dos puntos por el usuario, calcule la distancia entre estos dos puntos. 
'''
try:
        while True:
                print("Ingrese los valores de las coordenadas de dos puntos")
                punto1 = float(input("Ingrese el valor X del primer punto: "))
                punto2 = float(input("Ingrese el valor Y del primer punto: "))
                punto3 = float(input("Ingrese el valor X del segundo punto: "))
                punto4 = float(input("Ingrese el valor Y del segundo punto: "))
                if punto1 < 0 and punto2 < 0 and punto3 < 0 and punto4 < 0:
                        print("No ingrese valores negativos")
                break;
        distancia = ((punto1 - punto3)**2 + (punto2 - punto4)**2) ** 0.5
        print(f"La distancia entre los puntos: {distancia}")
except ValueError:
        print("Ingrese valor numérico")
        print(f"Error: {ValueError}")
