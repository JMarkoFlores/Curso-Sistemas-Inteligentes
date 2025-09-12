'''
3)La gaseosa en la planta embotelladora se almacena en tanques cilíndricos de un radio de 2 metros. Se necesita un programa que ingresando la altura hasta la que llega la gaseosa, calcule el volumen que se tiene. 
(Volumen del cilindro = Pi * radio2* altura) 
'''

try:
        while True:
                altura = int(input("Ingrese la altura (en m): "))
                if altura > 0:
                        break;
                else:
                        print("Ingrese un valor positivo mayor que 0")
        radio = 2
        pi = 3.1415
        volumen = pi * (radio ** 2)* altura
        print(f"El volumen del cilindro: {volumen}")
except ValueError:
        print("Ingrese un valor numerico")
        print(f"Error: {ValueError}")
