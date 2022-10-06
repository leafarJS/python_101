"""
Since Zortan has less gravity, residents can fly if they weight
less than or equal to 15 kgs in Zortan weight.
jorge wants to see which of his friends can fly.
Info:
-----
Our functions do only one thing at a time, this is called as `Single Responsibility Principle` and important aspect of programming.
"""
""" 
Como Zortan tiene menos gravedad, los residentes pueden volar si pesan
menor o igual a 15 kgs en peso Zortan.
jorge quiere ver cual de sus amigos puede volar.
Información:
-----
Nuestras funciones hacen solo una cosa a la vez, esto se denomina "Principio de responsabilidad única" y es un aspecto importante de la programación.
"""
from typing import Final
#const
MAX_FLYING_WEIGHT: Final[float] = 15


def calc_weight(weight: float) -> float:
  #calculates zortan weight
  #look how the function just transforms data, from float to float 
  return (weight + 32) / 8


def can_fly(weight: float) -> bool:
  #returns if you can fly
  #this function is a nice example for data transformation, we convert float values to boolean values!! nice isn't it!!
  return weight <= MAX_FLYING_WEIGHT



def flying_friends(friends: dict[str, float]) -> None:
  #display flying and non-flying friends 
  """
  Note: 
  No data transformation here.
  we are printing the output to console, the function doesn't return anyting. 
  """
  for name,earth_weight in friends.items():
    zortan_weight = calc_weight(earth_weight)
    if can_fly(zortan_weight):
      print(f"{name}: {zortan_weight} kgs can fly on Zortan!!")
    else:
      print(f"{name}: {zortan_weight} kgs can only walk on Zortan")


def main() -> None:
  friends: dict[str, float] = {
    "caca": 54,
    "cece": 88,
    "cici": 50,
    "coco": 102,
    "cucu": 94,
  }
  flying_friends(friends)

#invoke  the main function 
main()