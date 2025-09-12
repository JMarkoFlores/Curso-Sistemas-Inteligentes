'''
9) Construya una aplicación que determine cuanto se le debe cobrar a los clientes de un grifo, dado que los surtidores registran lo que venden en galones, pero el precio de la gasolina está fijado en litros. Cada galón tiene 3.785 litros. El precio del litro es S/ 3.86. 
'''
try:
        while True:
                galones = float(input("Ingrese la cantidad de galones: "))
                if galones > 0:
                        print("Numero válido") 
                        break;
                else:
                        print("Ingrese numero enteros positivos")
        plitro = 3.86
        litro = galones * 3.785
        pago = litro * plitro
        print(f"Valor a pagar: {pago}")
except ValueError:
        print("Ingrese valor numérico enteros positivos")
        print(f"Error: {ValueError}")
        