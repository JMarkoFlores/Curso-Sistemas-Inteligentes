'''
1) Hacer un programa para que se ingresen 2 números y reporte su suma, resta y multiplicación. 
'''
try:
        num1 = int(input("Ingrese primero número: "))
        num2 = int(input("Ingrese segundo número: "))
        suma = num1 + num2
        resta = num1 - num2
        mult = num1 * num2
        print(f"La suma de los números: {suma}")
        print(f"La resta de ({num1}) - ({num2}): {resta}")
        print(f"La multiplicación: {mult}")
except ValueError:
        print("Ingrese valor númerico")
        print(f"Error: {ValueError}")