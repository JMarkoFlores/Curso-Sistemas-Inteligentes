'''
4) Usando diccionarios:
Codifica un programa que permita guardar los nombres de los alumnos y las notas. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. 

#Al final, mostrar como hizo el profe en ejercicio 06
Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.  
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error. 

listaALumnos = { "nombre": (notas,...), "nombre2": (notas, ...)}
lista = [{nombre: promedio}]
'''

def inicio() :
        while True:
                try:
                        num = int(input("Ingrese la cantidad de alumnos: "))
                        if num > 0:
                                break
                        else:
                                print("Ingrese valores positivos enteros")
                except ValueError as e:
                        print("Error: Ingrese valores numericos")
                        print(f"Error: {e}")
        #print("Entrada exitosa")
        print()
        return num

#poner que si el nombre ya está que nos bote error
def pedir_nombre(lista):
        vacio = False
        while True:
                nombre = input("Nombre: ")
                if nombre.strip() == "":
                        print("Es obligatorio ingresar nombre")
                        continue
                if nombre in lista:  
                        print("ERROR: Ese nombre ya existe, ingrese otro")
                        continue
                else:
                        break
        return nombre 

def pedir_nota():
        print("Ingrese notas hasta que que introduzcamos un número negativo")
        listaNotas = []
        while True:
                try:
                        nota = int(input("Nota: "))
                        if nota < 0:  
                                break
                        else:
                                listaNotas.append(nota)
                except ValueError:
                        print("Ingresa valores numericos entero !!!")
                        print(f"Error: {ValueError}")
        print(f"Notas del alumno: {listaNotas}")
        return listaNotas

def registroDatos(x):
        listaAlumnos = {}
        for i in range(x):
                print(f"Datos del alumno {i+1}:")
                nombre = pedir_nombre(listaAlumnos) #string
                nota = pedir_nota()     #lista
                #diccionario: clave (string) - valor (lista)
                listaAlumnos.update({nombre:nota})
                print()
        #print(listaAlumnos)
        return listaAlumnos

def calcularMediaNotas(lista):
        print("Listado de alumnos con su ponderado")
        for a in lista.keys():
                #print(f"Clave: {a} - Valor: {lista[a]}")
                n = len(lista[a])
                suma = 0
                for b in lista[a]:
                        suma = suma + b
                #print(suma)               
                if suma == 0:
                        print(f"Alumno: {a} -> Ponderado: 0")
                else:
                        ponderado = suma/n
                        print(f"Alumno: {a} -> Ponderado: {ponderado}")

n = inicio()
lista = registroDatos(n)
calcularMediaNotas(lista)
