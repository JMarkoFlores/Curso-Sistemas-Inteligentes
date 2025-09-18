'''
5)Programa para intercambiar el valor de 2 variables numericas. 
'''
try:
        while True:
                var1 = int(input('Ingrese el valor de la primera variable: '))
                var2 = int(input('Ingrese el valor de la segunda variable: '))
                if var1 >0 and var2>0:
                        print("Valores aceptados")
                        temp = var1
                        var1=var2
                        var2=temp
                        print(f"Nueva primera variable: {var1}")
                        print(f"Nueva segunda variable: {var2}")
                        break
                else:
                        print("Ingrese valores positivos")
except ValueError:
        print("Ingrese un número")
        print(f"Error: {ValueError}")
