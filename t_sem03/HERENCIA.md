#### HERENCIA:

1 - Acceso:
a) Hereda todo público (atributo) y protegido (\_atributo).
b) No hereda lo privado (\_\_atributo).

2 - Constructores:

a) El hijo no está obligado a llamar al constructor del padre, pero si no lo hace, no tendrá inicializados sus atributos.

3 - Métodos:

a) La clase hija tiene acceso a todos los atributos y métodos públicos/protegidos de la clase padre. No está obligada a usarlos → Puede sobrescribir (reescribir) algunos, puede ignorarlos si no los necesita o puede ampliarlos con super().
b) Si el padre es abstracto → debe implementar los métodos abstractos.

4 - Atributos:

a) Si el hijo define un atributo con el mismo nombre que el del padre, oculta al del padre.

5 - Tipos de herencia en Python:

a) Simple → 1 padre.
b) Múltiple → varios padres. (En herencia múltiple → debe seguir el orden MRO, obedece el la clase q primero fue declarada)
c) Jerárquica → un padre con varios hijos.
d) Multinivel → un hijo hereda de otro hijo (cadena).

6 - Diferentes ejemplos de tipos de herencia:

# Herencia simple

class Animal:
def mover(self): return "El animal se mueve"

class Perro(Animal):
def mover(self): return "El perro camina en 4 patas"

# Multinivel

class Cachorro(Perro):
def mover(self): return "El cachorro camina torpemente"

# Jerárquica

class Gato(Animal):
def mover(self): return "El gato camina sigilosamente"

# Múltiple

class Robot:
def mover(self): return "El robot rueda"

class Cyborg(Animal, Robot):
pass

print(Perro().mover()) # El perro camina en 4 patas
print(Cachorro().mover()) # El cachorro camina torpemente
print(Gato().mover()) # El gato camina sigilosamente
print(Cyborg().mover()) # El animal se mueve (MRO → Animal antes que Robot)
