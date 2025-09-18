'''
3) Ingresar una lista con la información de n libros donde cada elemento es una tupla que contiene (título, autor, año de publicación). Obtener una nueva lista de libros publicados después de 2000.
'''

def inicio() :
        num = pedir_int("Ingrese la cantidad de libros: ")
        print()
        return num

def registroDatos(x):
        listaLibros = []
        for i in range(x):
                print(f"Datos del libro {i+1}:")
                titulo = pedir_string("titulo")
                autor = pedir_string("autor")
                año = pedir_int("Año de publicación : ")
                libro = (titulo, autor, año)
                listaLibros.append(libro)
                print()
        #print(listaLibros)
        return listaLibros

def nuevaLista(lista):
        nuevalista = []
        for i in lista:
                if i[2] > 2000:
                        nuevalista.append(i)
        print("El nuevo listado: ")
        for i in nuevalista:
                print(f"Autor: {i[0]} -> Libro: {i[1]} -> Año de publicación: {i[2]}")

def pedir_string(x):
        while True:
                string = input(f"{x} : ")
                if (string.strip() != ""):
                        break
                else:
                        print(f"Es obligatorio ingresar {x}")
        return string

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

n = inicio()
lista= registroDatos(n)
nuevaLista(lista)