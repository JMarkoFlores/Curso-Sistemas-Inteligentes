'''
ATRIBUTOS PUBLICOS Y METODOS DENTRO DE METODOS
2) Crear una clase Trabajador con atributos nombre, precio hora y horas trabajadas. Donde se calcule el salario bruto (Precio hora x horas trabajadas) los impuestos que son el 12% del salario bruto y el salario neto (salario bruto - impuestos)
'''
class Trabajador:
        def __init__(self, name, ph, ht):
                self.nombre = name
                self.preciohora = ph
                self.horatrabajo = ht
        
        def __str__(self):
                cad1 = "Datos del trabajador: "
                cad2 = f"Nombre: {self.nombre}"
                cad3 = f"Hora trabajada: {self.horatrabajo}"
                cad4 = f"Precio de la hora: {self.preciohora}"
                return f" {cad1}\n {cad2} \n {cad3} \n {cad4}"
        
        def calcularSalarioBruto(self):
                sb = self.horatrabajo * self.preciohora
                return sb
        
        def calcularImpuesto(self):
                i = 0.12 * self.calcularSalarioBruto()
                return i
        
        def calcularSalarioNeto(self):
                a = self.calcularSalarioBruto() - self.calcularImpuesto()
                return a
        
prueba = Trabajador("Marko", 10, 10)
prueba.nombre = "Jean"
print(prueba)
print(f"Salario Bruto: {prueba.calcularSalarioBruto()}")
print(f"Impuestos: {prueba.calcularImpuesto()}")
print(f"Salario Neto: {prueba.calcularSalarioNeto()}")
'''
Consideraciones:
1)Cuando haces f"" estas manejando cadena 
'''