'''
ATRIBUTOS PUBLICOS, CONSTRUCTOR CON METODO Y DICCIONARIO
5) Crear una clase llamada Agenda que tenga como atributo un diccionario con nombre numero de telefono y numero de Cumpleaños de n personas. Que permita dado un nombre mostrar los datos de la persona 
'''

def cantidadDeValores(mensaje):
        while True:
                try:
                        n = int(input(mensaje))
                except ValueError:
                        print("Ingrese valores numéricos")
                else:
                        if n < 0:
                                print("Ingrese valores positivos enteros")
                        else:
                                break
        return n

class Agenda:
        def __init__(self):
                self.numero = cantidadDeValores("Ingrese la cantidad de números: ")
                self.diccionario = {}
                
        def ingresarDatos(self):
                for i in range(self.numero):
                        nombre = input("Ingrese nombre: ")
                        telefono = input("Ingrese telefono: ")
                        print("Fecha de cumpleaño: ")
                        dia = cantidadDeValores("Dia: ")
                        mes = cantidadDeValores("Mes: ")
                        año = cantidadDeValores("Año: ")
                        cumpleaño = (dia, mes, año)
                        if nombre not in self.diccionario.keys():
                                self.diccionario.update({ nombre: (telefono, cumpleaño)})
                print(self.diccionario)
                
        def busqueda(self):
                nombre = input("Ingrese nombre a buscar: ")
                #El "a" es una clave de la lista de claves
                #Analogia: "i" es un iterador en interaciones
                for a in self.diccionario.keys():
                        if nombre == a:
                                # print("Usuario encontrado")
                                # #('1', (2, 3, 4))
                                # print(self.diccionario[a])
                                # #1
                                # print(self.diccionario[a][0])
                                # #(2, 3, 4)
                                # print(self.diccionario[a][1])
                                # #2
                                # print(self.diccionario[a][1][0])
                                return f"Telefono: {self.diccionario[a][0]}\nFecha cumpleaño: {self.diccionario[a][1][0]}/{self.diccionario[a][1][1]}/{self.diccionario[a][1][2]}"
                                break
                
                
prueba = Agenda()
prueba.ingresarDatos()
print(prueba.busqueda())