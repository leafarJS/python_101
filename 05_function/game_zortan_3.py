
"""
Save Zortan:
------------
Let's convert the game logic into small functions.
Principles:
-----------
1. DRY - Don't Repeat Yourself -
================================
Try to keep your code as DRY as possible, group common functionality into individual functions.

2. SRP - Single Responsibility Principle -
==========================================
Ideally one function should be responsible for only one operation.

Note:
-----
We will also learn about global & local scope of variables (Using scratch pad)
"""
""" 
Guardar Zortan:
------------
Convirtamos la lógica del juego en pequeñas funciones.

Principios:
-----------
1. DRY - No te repitas -
================================
Trate de mantener su código lo más DRY posible, agrupe la funcionalidad común en funciones individuales.

2. SRP - Principio de Responsabilidad Única -
==========================================
Idealmente, una función debería ser responsable de una sola operación.

Nota:
-----
También aprenderemos sobre el alcance global y local de las variables (usando el bloc de notas)
"""
#Import the stuff we require
from random import randint
from typing import Final 

#__________________LIFE___________________#
#Helper variables
#Helper variables
hero_life: int = 0
villian_life: int = 0

def increment_hero_life(life: int) -> None:
  #increment hero life
  global hero_life
  hero_life += life
  
def decrement_hero_life(life: int) -> None:
  #decrement hero life
  global hero_life
  hero_life -= life
  
def increment_villian_life(life: int) -> None:
  #increment hero life
  global villian_life
  villian_life += life
  
def decrement_villian_life(life: int) -> None:
  #decrement hero life
  global villian_life
  villian_life -= life
#__________________HEROES___________________#

def get_all_super_heroes():
  # Super Heroes
  IRONMAN = {"name": "Ironman", "attack_power": 250, "life": 800}
  BLACKWIDOW = {"name": "Blackwidow", "attack_power": 100, "life": 600}
  SPIDERMAN = {"name": "Spiderman", "attack_power": 150, "life": 700}
  HULK = {"name": "Hulk", "attack_power": 300, "life": 1000}
  # All Super Heros
  super_heroes = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
  return super_heroes

def get_super_heroe(index:int) -> None:
  #returns super heroe from the given index
  super_heroe = get_all_super_heroes()
  if index < len(super_heroe):
    return super_heroe[index]
  else:
    return None

#__________________VILLIANS___________________#

def get_all_super_villians():
  # Super Villains
  THANOS = {"name": "Thanos", "attack_power": 400, "life": 1800}
  REDSKULL = {"name": "Redskull", "attack_power": 300, "life": 800}
  PROXIMA = {"name": "Proxima", "attack_power": 320, "life": 800}
  # All Super Heros
  super_villains = [THANOS, REDSKULL, PROXIMA]
  return super_villains


def get_super_villian(index:int) -> None:
  #returns super villian from the given index
  super_villian = get_all_super_villians()
  if index < len(super_villian):
    return super_villian[index]
  else:
    return None





#__________________MAIN LOGIC___________________#
def attack() -> None:
  #Attack
  for attack_num in range(3):
    #each interation get a new hero & villain
    heroe_index = randint(0,3)
    villian_index = randint(0,2)
    
    current_super_heroe = get_super_heroe(heroe_index)
    current_super_villian = get_super_villian(villian_index)
    
    if current_super_heroe and current_super_villian:
      #attack
      simulate_attack(attack_num, current_super_heroe, current_super_villian)
    else:
      print("Error |=> No superheroes or villains to fight.")
    

def simulate_attack(attack_num: int, superheroe, supervillian) -> None:
  #simulate the actual attack
  
  #set life
  increment_hero_life(superheroe['life'])
  increment_villian_life(supervillian['life'])

  print(f"Attack:{attack_num + 1} => {superheroe['name']} is going to fight with {supervillian['name']}")
  
  #actual attack
  decrement_hero_life(supervillian['attack_power'])
  decrement_villian_life(superheroe['attack_power'])
  
  #______________FINAL GAME STATUS_______________#
  
def win_or_loose() -> None:
  # declare helper messages 
  WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
  LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"
  
  #print a nice separatin line
  print("*=" * 70)
  
  #win or lose
  if hero_life >= villian_life:
    print(WIN_MSG)
  else:
    print(LOST_MSG)
    
#______________MAIN_______________#  

def main() -> None:
  #Start the game
  attack()
  win_or_loose()
  
  
#______________START GAME_______________# 
main()