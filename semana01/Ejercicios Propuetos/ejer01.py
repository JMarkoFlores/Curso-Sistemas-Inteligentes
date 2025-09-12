''' 
1) Calcular el perímetro, el área y la diagonal de un rectángulo si se ingresan el valor de sus 
lados. Diagonal: (lado1 ^ 2 + lado2 ^ 2) ^ (1/2)
lado1: 3cm
lado2: 4cm
diagonal: 5cm
perimetro: 14cm
area: 12 cm2
'''
import sys
try:
        lado1 = float(input('Ingrese valor del primer lado: '))
        lado2 = float(input('Ingrese valor del segundo lado: '))   
except ValueError:
        print('Ingrese un valor de tipo float')
        print('Error: ', ValueError)
        sys.exit(0)
        
area = lado1*lado2
perimetro = 2* (lado1 + lado2)
diagonal = (lado1**2 + lado2 ** 2)** (1/2)
print('Resultado Final: ')
print('Perimetro: ', perimetro)
print('Área: ', area)
print('Diagonal: ', diagonal)
'''
Consideraciones:
1)En Python no existe catch, se usa except.
2)Para poner return es dentro de una función.
3)try-except poner dentro de una funcion
'''
