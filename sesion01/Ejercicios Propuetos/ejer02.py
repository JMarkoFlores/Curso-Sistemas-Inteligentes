'''
2) Calcular el salario neto de un trabajador. Se debe leer el nombre, horas trabajadas, precio de la hora y sabiendo que los impuestos aplicados son el 10 por ciento sobre el salario bruto. 
sb = ph * ht 
sn = sb - 0.10 * sb 
'''

nombre = str(input('Ingrese el nombre: '))
ht = int(input('Ingrese cantidad de horas trabajadas: '))
ph = float(input('Ingrese el precio de la hora: '))
tasa = 0.1

sb = ht * ph
i = tasa * sb
sn = sb - i
print('Sueldo bruto: ', sb)
print('Sueldo neto: ', sn)



'''
Consideraciones:
0)Sintaxis 
0.1-Para funciones: Python usa "def", JS "function".
0.2-Cuando defines un método dentro de una clase, el primer parámetro SIEMPRE debe ser "self" para recibir la referencia al objeto actual.
1)Casting: int(), float(), str(), bool(), list(), tuple(), set()
2)Tipos de datos numéricos: int, float, complex(Para nº complejos)
3)Tipos de datos texto: str
4)Tipos de datos boolean: bool
5)Secuencias: 
5.1- Listas: son como arreglos pero permiten todo tipo de dato. Ex:
        frutas = ["manzana", 1, "uva", 2]
        frutas.append("plátano")
        print(frutas)
        print(frutas[1])
5.2- Array: solo permite un tipo de dato (import array)
5.3- Tupla: son listas imutables, agrupa datos de todos los tipos con ()
        coordenada = (40, "Jean", 4, 26)
        print(coordenada[0])  
        print(coordenada[1]) 
        print(coordenada[2])
5.4- Range: es el iterador del bucle for; solo es para generar secuencias de numeros. Su estrutura es: range(inicio, fin, paso); donde "inicio" es número inicial (por defecto 0); "fin" es número final (no incluido); "paso" es de cuánto en cuánto aumenta (por defecto 1). Ejemplo:
        for i in range(0, 11, 2):
                print(i)   # 0, 2, 4, 6, 8, 10
'''