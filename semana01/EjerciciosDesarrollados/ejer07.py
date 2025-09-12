'''
7) Dado un número natural de cuatro cifras, diseñe un algoritmo que forme un número con la cifra de los millares y la cifra de las unidades, en ese orden. Así, por ejemplo, si se ingresara el número 8235, el número formado sería 85. 
'''
try:
        while True:
                numero = int(input("Ingrese numero de 4 cifras: "))
                if numero > 999 and numero < 10000:
                        print("Numero válido") 
                        break;
                else:
                        print("Ingrese numero entre 1000 - 9999")
        millares = numero //1000
        unidades = numero % 10
        nuevoNumero = millares * 10 + unidades
        print(f"Numero transformado: {nuevoNumero}")
except ValueError:
        print("Ingrese valor numérico enteros")
        print(f"Error: {ValueError}")
        