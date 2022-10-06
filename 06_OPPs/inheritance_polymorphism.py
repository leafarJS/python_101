"""
Inheritance:
------------
All species inherit a lot from their parents, may be they have same eyes as their mother but different voice all together.
Python classes are no different, we can inherit from classes and make them share common functionality. 
At the same time we can dynamically add other features and functionality as well.
Polymorphism:
-------------
Suppose there are two children, one want's to speak in Marathi, other want's to speak in Sanskrit. This is possible using polymorphism! It's just creating the same methods but with different behavior.
"""
"""
Herencia:
------------
Todas las especies heredan mucho de sus padres, puede ser que tengan los mismos ojos que su madre pero una voz diferente todos juntos.
Las clases de Python no son diferentes, podemos heredar de las clases y hacer que compartan una funcionalidad común.
Al mismo tiempo, también podemos agregar dinámicamente otras características y funcionalidades.
Polimorfismo:
-------------
Supongamos que hay dos niños, uno quiere hablar en marathi, el otro quiere hablar en sánscrito. ¡Esto es posible usando polimorfismo! Es solo crear los mismos métodos pero con un comportamiento diferente.
"""
# TODO Clase padre, superior, molde , super
class Animal:
  
  def __init__(self,name:str, age:int, num_legs:int)-> None:
    self.name = name
    self.age = age
    self.num_legs = num_legs
    
  def __str__(self) ->str:
    return f"Name: {self.name}"
  
  def talk(self) -> None:
    #makes the animal talk
    print(f"{self.name} can't talk yet!")

# TODO Clase que hereda de la clase padre  
class Dog(Animal):
  
  def __init__(self,name:str, age:int, num_legs:int, breed:str):
    #take the commo features and pass to the parent(super) class
    super().__init__(name, age, num_legs)
    self.breed = breed
    self.type = "Dog"
    
  def __str__(self) ->str:
    #we alter the talk method and make it say woff adding polymophic behavior
    return f"Is the type: {self.type} | names is: {self.name}, breed is: {self.breed}"
  
  def talk(self) -> None:
    print(f"{self.name} says wofff...")
    
  def sniff(self, item:str) -> None:
    print(f"{self.name} is sniffing out {item}")
    
animal_one = Animal("Robbin", 10, 4)

print(animal_one)
animal_one.talk()

specifc_animal = Dog("whisky", age = 15, num_legs = 4, breed ="Ingland Old Pastor")

print(specifc_animal)
specifc_animal.talk()
specifc_animal.sniff("sheet")

#______________________________________________#

# TODO Clase que hereda de la clase padre  
class Cat(Animal):
  
  def __init__(self,name:str, age:int, num_legs:int, breed:str):
    #take the commo features and pass to the parent(super) class
    super().__init__(name, age, num_legs)
    self.breed = breed
    self.type = "Cat"
    
  def __str__(self) ->str:
    #we alter the talk method and make it say miauuu adding polymophic behavior
    return f"Is the type: {self.type} | names is: {self.name}, breed is: {self.breed}"
  
  def talk(self) -> None:
    print(f"{self.name} says miauuu...")
    
  def sniff(self, item:str) -> None:
    print(f"{self.name} is sniffing out {item}")
    
specifc_animal = Cat("Garfield", age = 8, num_legs = 4, breed ="Siames")

print(specifc_animal)
specifc_animal.talk()
specifc_animal.sniff("dinner")

#______________________________________________#

# TODO Clase que hereda de la clase padre  
class Dinosaur(Animal):
  
  def __init__(self,name:str, age:int, num_legs:int, breed:str):
    #take the commo features and pass to the parent(super) class
    super().__init__(name, age, num_legs)
    self.breed = breed
    self.type = "Dinosaur"
    
  def __str__(self) ->str:
    #we alter the talk method and make it say Grrrrmm!!! adding polymophic behavior
    return f"Is the type: {self.type} | names is: {self.name}, breed is: {self.breed}"
  
  def talk(self) -> None:
    print(f"{self.name} says Grrrrmm!!!")
    
  def sniff(self, item:str) -> None:
    print(f"{self.name} is sniffing out {item}")
  
  def hunt(self) -> None:
    print(f"{self.name} is out for hunting...")
    
specifc_animal = Dinosaur("T-Rex", age = 40, num_legs = 2, breed ="Saurus")

print(specifc_animal)
specifc_animal.talk()
specifc_animal.hunt()
specifc_animal.sniff("other dinosaur")


#_____________________________________________
print(isinstance(specifc_animal, Animal))

print("================================")
print(isinstance(specifc_animal, Dog))
print(isinstance(specifc_animal, Cat))
print(isinstance(specifc_animal, Dinosaur))

