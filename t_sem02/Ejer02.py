'''
2)Ingresar el nombre y las notas de los alumnos de programación en una lista de tuplas. Luego buscar un nombre y mostrar su nota si se encuentra. Además, mostrar la lista en orden alfabético.
'''
def inicio() :
        while True:
                try:
                        num = int(input("Ingrese la cantidad de estudiantes: "))
                        if num > 0:
                                break
                        else:
                                print("Ingrese valores positivos enteros")
                except ValueError as e:
                        print("Error: Ingrese valores numericos")
                        print(f"Error: {e}")
        #print("Entrada exitosa")
        return num

def registroDatos(x):
        listaAlumnos = []
        for i in range(x):
                print(f"Datos del alumno {i+1}:")
                nombre = pedir_nombre()
                nota = pedir_nota()
                alumno = (nombre, nota)
                listaAlumnos.append(alumno)
        #print(listaAlumnos)
        return listaAlumnos

def pedir_nombre():
        while True:
                nombre = input("Nombre: ")
                if nombre.strip() != "":
                        break
                else:
                        print("Es obligatorio ingresar nombre")
        return nombre               
def pedir_nota():
        while True:
                nota = input("Nota (opcional): ")
                if nota.strip() == "":  
                        nota = None
                        break
                else:
                        try:
                                nota = float(nota)   
                                break
                        except ValueError:
                                print("Ingresa valores numericos !!!")
        return nota

def buscarAlumno(lista):
        print("------------------")
        print("INICIO DE BÚSQUEDA")
        nombre = input("Ingrese el nombre: ")
        print()
        encontrado = False
        for i in lista: 
                if nombre == i[0]:
                        print("Alumno encontrado")
                        if i[1] != None:
                                print(f"Nota: {i[1]}")
                        else:
                                print(f"El alumno ' {i[0]} ' no tiene nota")
                        encontrado = True
                        break
        if encontrado == False:
                print("Ese alumno no está registrado")
        return lista
                
def ordenando(lista):
        print("------------------")
        print("ORDENANDO LA LISTA ")
        for i in range(len(lista)): 
                j=len(lista)-1 
                while j>i: 
                        if lista[j][0]<lista[j-1][0]: 
                                lista[j], lista[j-1] = lista[j-1],lista[j] 
                        j=j-1
        for e in lista:
                print(f"Nombre: {e[0]} -> Nota: {e[1]}")

print("Ejecutando programa")
numero = inicio()
listado = registroDatos(numero)
busqueda = buscarAlumno(listado)
ordenando(busqueda)