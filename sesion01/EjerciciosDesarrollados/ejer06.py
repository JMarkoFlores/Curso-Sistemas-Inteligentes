'''
6) Dada una cantidad de dinero en soles, diseñe un programa que descomponga dicha cantidad en billetes de S/. 100, S/. 50, S/.10 y monedas de S/. 5, S/. 2 y S/.1. Así, por ejemplo, S/. 3778 puede descomponerse en 37 billetes de S/. 100, más 1 billete de S/. 50, más 2 billetes de S/. 10, más 1 moneda de S/. 5, más 1 moneda de S/.2 y más 1 moneda de S/. 1. 
'''

try:
        while True:
                dinero = int(input("Ingrese el monto entero a descomponer: "))
                if dinero > 0:
                        break
                else:
                        print("Ingrese valores positivos no nulos")            
        cien = dinero // 100      
        cinc = (dinero % 100) // 50   
        diez = ((dinero % 100) % 50) // 10 
        cinc = (((dinero % 100) % 50) % 10 ) // 5
        dos = ((((dinero % 100) % 50) % 10 ) % 5 ) // 2
        uno = ((((dinero % 100) % 50) % 10 ) % 5 ) % 2 
        notas = [cien, cinc, diez, cinc, dos, uno]
        valores = [100, 50, 10, 5, 2, 1]

        print("Descomponiendo la plata")
        for i in range(len(notas)): 
                if notas[i] > 0:       
                        print(f"Billetes de S/{valores[i]} : {notas[i]}")
except ValueError:
        print("Ingrese valor numérico enteros")
        print(f"Error: {ValueError}")
        
'''
consideraciones:
1)Cantidad de una lista: len(nombreLista)
2)range(6): genera i de 0 a 5
'''