'''
1) Ingresar una lista con la información de n estudiantes, donde cada elemento de la lista es una tupla que contiene el nombre del estudiante y una lista con las 3 calificaciones del estudiante. Calcular el promedio de calificaciones para cada estudiante y crea una nueva lista de tuplas con el nombre del estudiante y su promedio.
'''

def pedir_int(x):
        while True:
                try:    
                        i = int(input(x))    
                        if i > 0:
                                break
                        else:
                                print("Ingrese valores positivos")
                except ValueError:
                        print("Ingrese valores numéricos")
                        print(f"Error: {ValueError}")
        return i

def pedir_float(x):
        while True:
                try:    
                        i = float(input(x))    
                        if i > 0:
                                break
                        else:
                                print("Ingrese valores positivos")
                except ValueError:
                        print("Ingrese valores numéricos")
                        print(f"Error: {ValueError}")
        return i

def registroDatos(x):
        lista = []
        for i in range (x):
                notas = []
                print(f"Ingrese datos del aluno {i + 1} :")
                nombre = input("Ingrese nombre: ")
                for i in range(x):
                        nota = pedir_float(f"Ingrese nota de la calificación {i + 1}: ")
                        notas.append(nota)
                tupla = (nombre, notas)
                lista.append(tupla)
                print()
        return lista

def nuevaLista(lista):
        nuevalista = []
        print("Los promedios de cada alumno registrado: ")
        print()
        for i in range(len(lista)):
                print(f"Nombre del alumno {i+1} : {lista[i][0]}")
                suma = 0
                for j in lista[i][1]:
                        suma = suma + j
                promedio = suma/3
                print(f"Promedio: {promedio}")
                nuevaTupla = ({lista[i][0]}, promedio)
                nuevalista.append(nuevaTupla)
                print()

n = pedir_int("Ingrese la cantidad de estudiantes: ")
lista = registroDatos(n)
nuevaLista(lista)
