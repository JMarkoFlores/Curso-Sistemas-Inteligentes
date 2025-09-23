def validacionesFloat(mensaje):
        while True:
                try:
                        n = float(input(mensaje))
                except ValueError:
                        print("Ingrese valores numéricos")
                else:
                        if n < 0:
                                print("Ingrese valores positivos")
                        else:
                                break
        return n

def validacionesInt(mensaje):
        while True:
                try:
                        n = int(input(mensaje))
                except ValueError:
                        print("Debes ingresar un numero entero")
                else:
                        if n > 0:
                                return n 
                        else:
                                print("Debes ingresar un número positivo")