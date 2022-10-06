"""
Class:
------
`Class` are just like a building blueprint, they provide you with the specifications of how to construct a building. It is upto you when and
how you build the building.

Instance:
---------
When you actually construct a building out of the blueprint, it is called as an `Instance` or `Object` of the class. So, both are related but essential different terminology.
Class = Blueprint, Instance = Building

Methods:
--------
These are just normal functions, but defined to alter the behavior of your instance or class.
Since they are tied to a class, they are called as methods. Their behavior is dependent on the structure you define in the class.

When to use Class:
------------------
Use classes only when you need `Structure` and `Behavior` together.
If you only need structure, then choose from any existing data structures such as list, tuple, dictionary, queue, etc. Just need a behavior? Then just create a function
that transforms your data.
"""
""" 
Clase:
------
Las "clases" son como un plano de construcción, te brindan la especificaciones de cómo construir un edificio. Depende de ti cuándo y cómo se construye el edificio.

Instancia:
---------
Cuando realmente construyes un edificio a partir del plano, se llama como una `Instancia` u `Objeto` de la clase. Entonces, ambos están relacionados pero son esenciales.
terminología diferente.
Clase = Plano, Instancia = Edificio

Métodos:
--------
Estas son solo funciones normales, pero definidas para alterar el comportamiento de su instancia o clase.
Dado que están vinculados a una clase, se denominan métodos. Su comportamiento depende de
la estructura que defina en la clase.

Cuándo usar Clase:
------------------
Use clases solo cuando necesite 'Estructura' y 'Comportamiento' juntos.
Si solo necesita una estructura, elija entre las estructuras de datos existentes, como
lista, tupla, diccionario, cola, etc. ¿Solo necesita un comportamiento? Entonces solo crea una función que transforma sus datos.
"""

class SomeClass:
  #defines an empty class
  pass

print(SomeClass)


#___________________________________________#

class Person:
  #define a person
  def __init__(self, first_name:str, last_mane:str)-> None:
    #this special method represent a constructor
    self.first_name = first_name
    self.last_name = last_mane
    
  def __repr__(self) -> str:
    return '<class "Person">'
  
  def __str__(self) -> str:
    #this magig method provides string representation of an instance.
    return f"A person is: {self.first_name} {self.last_name}"
  
  def greet(self) -> None:
    #Method that prints a greating message
    print(f"{self.first_name} says Hello 👋")

#create an 'instance' of class/type 'Person'
person_one = Person("jorge","callejo")
person_two = Person("rafael","flores")

print(person_one)
print(person_two)

print(person_one.first_name)
print(person_two.first_name)

print(f"my direction in memory is: {hex(id(person_one.first_name))}")
print(f"my direction in memory is: {hex(id(person_two.first_name))}")

#possible but not recommended
print(person_one.__init__())
print(person_two.__init__())

#calling methods on particular instance
person_one.greet()
person_two.greet()

