"""
Variable & Keyword Arguments:
-----------------------------
What happens if we don't know before hand how many arguments we are going to receive? We can handle this situation by using variable &
keyword arguments syntax.
Info:
-----
We will first look at unpacking first.
"""
""" 
Argumentos de variables y palabras clave:
--------------------------------------------
¿Qué pasa si no sabemos de antemano cuántos argumentos vamos a recibir? Podemos manejar esta situación usando la variable & sintaxis de argumentos de palabra clave.
Información:
-----
Primero veremos el desempaque primero.
"""
# ------- Unpacking------------#
from typing import Any

#Tuple
fname, lname = ("jorge", "rafael")
print(fname)
print(lname)

#list 
first, *rest = ["caca", "cece", "cici", "coco", "cucu"]
print(first)
print(rest)

#dict
specifics = {
  "type":"dinamic",
  "optional":"static typing",
  "found":"everywhere"
}

lang = {
  "name": "python",
  **specifics
}
print(lang)

#--------------Variable arguments-------------#

def unknow_friends(*args:str) -> None:
  for friend in args:
    print(friend)
    
unknow_friends(rest)
unknow_friends("caca", "cece", "cici", "coco", "cucu")

#--------------keyword arguments-------------#

def unknown_product(**kwargs):
  for k, v in kwargs.items():
    print(f"{k} : {v}")
    
order = {
  "name":"pizza",
  "price":3.99,
  "toppping":"olives",
  "extra_cheese":True
}
unknown_product(name="pizza", price=3.99, toppping="olives",extra_cheese=True)
# jorgeunknown_product(order) #no pass dict

#--------------Together-------------#
def invoice(product: str, *args, **kwargs) -> None:
  print(product)
  print(args)
  print(kwargs)


invoice("milk", rest, extra_cheese=True)