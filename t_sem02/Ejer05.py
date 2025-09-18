'''
5) Usando diccionarios. 
Un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú: 
A) Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
B) Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena. 
C) Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda. 
D) Listar: Nos muestra todos los contactos de la agenda.
'''
def menu() :
        while True:
                try:
                        print("\nIngrese una de las opciones del menu:\n1 - Añadir/Modificar\n2 - Buscar\n3 - Borrar\n4 - Listar\n5 - Salir")                        
                        num = int(input("Ingrese una de las opciones (1-5): "))
                        print()
                        if num > 0 and num < 6:
                                break
                        else:
                                print("ERROR: Ingrese valores del rango de 1 - 5\n")
                except ValueError as e:
                        print("\nError: Ingrese valores numericos")
                        print(f"Error: {e}\n")
        return num

def pedir_nombre(mensaje):
        while True:
                nombre = input(mensaje)
                if nombre.strip() == "":
                        print("Es obligatorio ingresar nombre")
                else:        
                        break
        return nombre

def pedir_telefono(mensaje):
        while True:
                tel = input(mensaje)
                if len(tel) == 9:
                        break;
                else:        
                        print("El telefono debe contener 9 cifras")
        return tel

def pregunta(mensaje):
        while True:
                opcion = input(mensaje)
                if opcion.lower() == "s" or opcion.lower() == "n":
                        break
                else:
                        print("Ingrese: S o N")
        return opcion

def main():        
        agenda = {}  
        while True:
                opcion = menu()
                if opcion == 1:
                        opcion1(agenda)
                elif opcion == 2:
                        opcion2(agenda)
                elif opcion == 3:
                        opcion3(agenda)
                elif opcion == 4:
                        opcion4(agenda)
                elif opcion == 5:
                        print("Finalizando la aplicación...")
                        break

def opcion1(x):
        encontrado = False
        nombre = pedir_nombre("Ingrese nombre: ")
        for a in x.keys():
                if a == nombre:
                        print(f"Telefono: {x[a]}")
                        opcion = pregunta("Deseas modificar el telefono (S o N): ")
                        if opcion.lower() == "s":
                                t = pedir_telefono("Ingrese nuevo telefono (9 cifras): ")
                                x.update({a : t})        
                        encontrado = True
        if encontrado == False:
                telefono = pedir_telefono("Ingrese Telefono (9 cifras): ")
                x.update({nombre:telefono}) 
        print(x)

def opcion2(x):
        print("soy opcion 2")
        string = pedir_nombre("Ingrese cadena de caracteres: ")
        encontrado = False
        for a in x.keys():
                if a.startswith(string):
                        print(f"Telefono: {x[a]} -> nombre: {a}")
                        encontrado = True
        if encontrado == False:
                print(f"No se encontro usuario que comiencen con '{string} ' ")

def opcion3(x):
        print("soy opcion 3")
        encontrado = False
        nombre = pedir_nombre("Ingrese nombre: ")
        for a in x.keys():
                if a == nombre:
                        encontrado = True
                        opcion = pregunta("Deseas eliminar ese usuario (S o N): ")
                        if opcion.lower() == "s":
                                del x[nombre]
                                break
        if encontrado == False:
                print("Este usuario no existe")
        print(x)
        
def opcion4(x):
        print("Listado de telefono: \n")
        if len(x) == 0:
                print("No existe usuarios en la agenda")
        else:
                for a in x.keys():
                        print(f"Telefono: {x[a]} -> Nombre: {a}")
        
main()