'''
4) Dado un número natural de 4 cifras, hacer un programa que determine la suma y el 
producto de las cifras del número. 
'''
#Para ingresar un número + 
'''
while True:
        try:
                numero = int(input('Ingrese número: '))
                if numero>0:
                        print(f"Número {numero} válido")
                        break
                else:
                        print('Ingrese un número positivo')
        except ValueError:
                print('Ingrese número')
                print(f"Error: {ValueError}")
'''
while True:
        try:
                numero = int(input('Ingrese número de 4 cifras: '))
                if numero>999 and numero<10000:
                        print(f"Número {numero} de 4 cifras")
                        def cifras(numero, suma, prod):
                                #print('Ejecutando funcion cifras con ',numero)
                                while True:
                                        if numero>0:
                                                frag = numero % 10
                                                #print(f"frag: {frag}")
                                                suma = suma + frag
                                                #print(f"suma: {suma}")
                                                prod = prod * frag
                                                #print(f"producto: {prod}")
                                                return cifras(numero//10, suma, prod)
                                        else:
                                                print(f"Suma de las cifras: {suma}")
                                                print(f"Producto de las cifras: {prod}")
                                                break
                        cifras(numero, 0, 1)
                        break
                else:
                        print('Ingrese número positivo de 4 cifras')
        except ValueError:
                print('Ingrese número')
                print(f"Error: {ValueError}")


'''
Consideraciones:
1)"Do...While" no existe en python
2)"While" si existe (normal)
3)"For" si existe y la iteracion se hace con "range"
4)"For...in" sirve para recurrir todo de sentencias (listas[arreglo más potente], tuplas(listas inmutables)). En JS: recurre objeto (fornit)
5)"For...of" no existe en python. En JS recurre arreglo (for oposto of)
6)"Switch" no existe en python: para eso utiliza if xxx:...elif xxxx:...else:



'''