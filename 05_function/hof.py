""" 
Higher Order Functions:
-----------------------
Please note that this is a advanced topic, so it may take a couple of attempts to understand these concepts.

Functions under the hood are just `Objects`, they can be passed to other functions and functions can also return functions!

This data type is called as `Callable`, one which can be called or invoked.

Note:
-----
Till now we have been sending data to our functions, but sending data every time can be expensive, instead we can send function to data!
Don't spend too much time mastering this topic, it will come naturally as you progress with your programming skills.
"""
"""
Funciones de orden superior:
-----------------------
Tenga en cuenta que este es un tema avanzado, por lo que puede tomar un par de intentos para comprender estos conceptos.

Las funciones bajo el capucha son solo 'Objetos', se pueden pasar a otras funciones y funciones también pueden devolver funciones!
Este tipo de datos se llama `Callable`, uno que se puede llamar o invocar.

Nota:
-----
Hasta ahora hemos estado enviando datos a nuestras funciones, pero enviando datos cada vez puede ser costoso, ¡en su lugar podemos enviar la función a los datos!
No dedique demasiado tiempo a dominar este tema, le resultará natural a medida que progresar con sus habilidades de programación.
"""
from typing import Callable
def hello()->None:
  #print message
  print("Hello World")


#hello is jus a regular object or class of type 'funtion'
""" 
print(hello)
print(id(hello))
print(type(hello)) 

"""

#we can assing function to variables


# just assing the object 'hello' to greet variable
greet: Callable[[], None] = hello


#we can invoke / call the function using () at the end
#greet()



#let's try to create a universal greeter that can greet a person in mutiple ways 

def zola(name: str) -> str:
  return f"Zola, {name}"

def good_morning(name: str) -> str:
  return f"good morning, {name}"

def goodbye(name: str) -> str:
  return f"Goodbye, {name}"

#function accepting a function 
def universal_greeter(name:str, greeter: Callable[[str], str]):
  #can greet in multiple way
  msg = greeter(name)
  print(msg)


universal_greeter("jorge", zola)
universal_greeter("jorge", good_morning)
universal_greeter("jorge", goodbye)

#--------------------------------------------------

""" 
Function returing functions!!!

this can be confusing, relax if you can't get it, it took me several attemps to understand this!
"""

def add_by_5(num:int)-> Callable[[], int]:
  #add by 5
  def by_5()-> int: 
    return num + 5
  
  return by_5

sum = add_by_5(10)
print(sum())


#function returning a function
def unique_adder(num1:int)-> Callable[[], int]:
  #adds two numbers and then subtract 1
  def adder(num2:int) -> int: 
    return num1 + num2 - 1
  
  return adder


result = unique_adder(100)
print(result(5))


# ----------------------------------------------

"""
Lambda:
-------
Perhaps the most neglected, but very powerful technique to work with functions.
Again, don't spend too much time mastering it, it will come naturally!

The way in which we declared functions are very verbose, we can condense them in a single statement.

Let's try to create a calculator from scratch
"""
"""
lambda:
-------
Quizás la técnica más olvidada, pero muy poderosa para trabajar con funciones.
Una vez más, no dedique demasiado tiempo a dominarlo, ¡saldrá de forma natural!
La forma en que declaramos las funciones es muy detallada, podemos condensarlas en una sola declaración.
Intentemos crear una calculadora desde cero.
"""

add: Callable[[int,int], int] = lambda num1, num2: num1 + num2
rest: Callable[[int,int], int] = lambda num1, num2: num1 - num2
product: Callable[[int,int], int] = lambda num1, num2: num1 * num2

def calc(num1:int,num2:int, operation:Callable[[int,int], int]) -> int:
  return operation(num1,num2)

print(calc(4,5, add))
print(calc(4,5, rest))
print(calc(4,5, product))