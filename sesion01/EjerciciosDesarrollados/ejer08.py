'''
8) Dado un número natural de tres cifras, diseñe un algoritmo que permita obtener el revés del número. Así, si se ingresa el número 238 el revés del número es 832. 
'''
try:
        while True:
                numero = int(input("Ingrese numero de 3 cifras: "))
                if numero > 99 and numero < 1000:
                        print("Numero válido") 
                        break;
                else:
                        print("Ingrese numero entre 100 - 999")
        238
        centenas = numero // 100
        dezenas = (numero % 100) // 10
        unidades = numero % 10
        nuevoNumero = unidades * 100 + dezenas * 10 + centenas
        print(f"Numero transformado: {nuevoNumero}")
except ValueError:
        print("Ingrese valor numérico enteros")
        print(f"Error: {ValueError}")
        