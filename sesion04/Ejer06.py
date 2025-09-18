'''
• Programa para calcular los promedios de alumnos. 
• El programa pide el nombre del alumno seguido de su calificación. 
• Los nombres son ingresados en cualquier orden. 
• El ingresar la palabra exit da por terminado el ingreso de nombres. (RESTRICCIÓN)
• Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final. 

LÓGICA EMPLEADA:
1) Uso de diccionario para ingresar los datos: el nombre del alumno como clave y que todas las calificaciones asociadas son almacenadas en una tupla como valor.
2) Si el nombre es exit, salimos del bucle. 
3) Si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=).
4) Si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada. 
5) Al final se calcula e imprime el promedio del alumno junto con su nombre.
'''
#Las tuplas osn modificable si haces operacion como (+) o (*). Se puede verificar ciertos valor con "in" o "not in"
grupo = {} 
while True: 
        #Al inicio solo añades un nombre y una nota. Si ingresa un nombre que ya existe en el diccionario, la nota ingresada se añade con la nota anterior que ya ingresaste. El programa se cierra cuando ingreses "exit" en nombre.
        nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ") 
        if nombre == 'exit': 
                break 
        calif = int(input("Ingresa la calificación del alumno (0-10): ")) 
        #Si se ingresa un nombre ya existente, añade nuevas notas 
        if nombre in grupo: 
                grupo[nombre] += (calif,) 
        else: 
                #Es la forma de ingresar valor. Puedes poner un string o una lista o otro objeto
                grupo[nombre] = (calif,)
        #Para iterar sobre el diccionario
        #keys() nos dá una lista de clave: nombre es el clave y cuando haces grupo[clave] te muestra el valor q en ese caso creo q es una tupla; El sorted solo es para poner en orden cresciendo las clave.
        for nombre in sorted(grupo.keys()): 
                sum = 0 
                contador = 0 
                for calif in grupo[nombre]: 
                        sum += calif 
                        contador += 1 
                print(nombre, ":", sum / contador) 
print(grupo) #{'J': (2, 3) , 'M': (3,) , 'F': (1, 2)}