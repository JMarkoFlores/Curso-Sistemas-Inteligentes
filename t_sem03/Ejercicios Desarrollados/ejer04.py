'''
ATRIBUTOS PUBLICOS, CONSTRUCTOR CON METODO Y LISTA, FUNCIONES MIN/MAX/SORTED/SORT
4) Crear una clase llamada ListaReales que tenga como atributos una lista de numeros reales y que permita ingresar datos a a la lista, calcular el mayor, el menor, el promedio y ordenar la lista en forma ascendente y descendente 
'''

def leerNumeroEntero(mensaje):
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
                                
class ListaReales:
        def __init__(self):
                self.numero = leerNumeroEntero("Ingrese la cantidad de número a ingresar: ")
                self.lista = []
        
        def ingresarDatos(self):
                for i in range(self.numero):
                        while True:
                                try:
                                        numero = float(input("Número:"))
                                        break
                                except ValueError:
                                        print("Ingrese valores numéricos")
                        self.lista.append(numero)
                print(self.lista)
                
        def calcularMayor(self):
                # mayor = self.lista[0]
                # #El "i" es solo iterador
                # for i in range(self.numero):
                #         if self.lista[i] >= mayor:
                #                 mayor = self.lista[i]
                # return mayor
                return max(self.lista)
        
        def calcularMenor(self):
                # menor = self.lista[0]
                # #El "i" es solo iterador
                # for i in range(self.numero):
                #         if self.lista[i] <= menor:
                #                 menor = self.lista[i]
                # return menor
                return min(self.lista)
        
        def calcularPromedio(self):
                promedio = sum(self.lista)/len(self.lista)
                return promedio
        
        def ordenAscendiente(self):
                #self.lista.sort()
                return sorted(self.lista)

        def ordenDescendiente(self):
                #self.lista.sort(reverse=True)
                return sorted(self.lista, reverse=True)
                
prueba = ListaReales()
prueba.ingresarDatos()
print(f"El mayor: {prueba.calcularMayor()}")
print(f"El menor: {prueba.calcularMenor()}")
print(f"El promedio: {prueba.calcularPromedio()}")
print(f"En orden ascendiente: {prueba.ordenAscendiente()}")
print(f"En orden descendiente: {prueba.ordenDescendiente()}")

'''
Consideraciones:
1)Usa .sort() si:
A- Solo trabajas con listas.
B- No te importa que la lista original cambie.
C- Quieres ahorrar memoria (porque no crea una copia).

2)Usa sorted() si:
A- Necesitas mantener intacta la lista original.
B- Quieres usarlo con otras estructuras (tuplas, sets, diccionarios).
C- Prefieres un estilo más funcional (devuelve un valor).

'''