'''
4) Dado un número natural de 4 cifras, hacer un programa que determine la suma y el 
producto de las cifras del número. 
'''

while True:
        try:
                numero = int(input('Ingrese número de 4 cifras: '))
                if numero > 999 and numero < 10000:
                        print(f"Número {numero} de 4 cifras")
                        suma = 0
                        prod = 1
                        temp = numero  
                
                        while temp > 0:
                                cifra = temp % 10   
                                suma += cifra
                                prod *= cifra
                                temp //= 10       
                        
                        print(f"Suma de las cifras: {suma}")
                        print(f"Producto de las cifras: {prod}")
                        break
                else:
                        print('Ingrese número positivo de 4 cifras')
        except ValueError:
                print("Error: debe ingresar un número válido")
                
'''
Consideraciones:
1)Para q el "while" torne recursivo se tiene que retornar terminar la logica con la misma variable que está en la condicion... pero q valga diferente sino se tiene un bucle infinito
'''
