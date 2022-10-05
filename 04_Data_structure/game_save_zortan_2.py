"""
Save Zortan:
------------
The war has just intensified, Thanos army has reach Zortan and are going to fight along with him. With his army, this time Thanos is going to attach Avengers and the battle is going to be intense!!!

Since, everything is going in real-time, we don't have control over characters, instead our characters will choose their own fight.

This time each character gets it own structure and defined parameters, so as you can see our code is getting better and certainly we are going to make is awesome as we progress with future modules.
"""

"""
Guardar Zortan:
------------
La guerra acaba de intensificarse, el ejército de Thanos ha llegado a Zortan y van a luchar junto con él. Con su ejército, esta vez Thanos se unirá a los Vengadores y la batalla va a ser intensa!!!

Dado que todo ocurre en tiempo real, no tenemos control sobre los personajes, en cambio, nuestros personajes elegirán su propia pelea.

Esta vez cada personaje tiene su propia estructura y parámetros definidos, así que podemos ver que nuestro código está mejorando y ciertamente lo vamos a hacer es increíble a medida que avanzamos con futuros módulos.
"""
from random import randint
from typing import Final

#alias para no ser repetitivos cuando los diccionarios tienen la misma estructura 


# Super Heroes
IRONMAN = {"name": "Ironman", "attack_power": 250, "life": 800}
BLACKWIDOW = {"name": "Blackwidow", "attack_power": 100, "life": 600}
SPIDERMAN = {"name": "Spiderman", "attack_power": 150, "life": 700}
HULK = {"name": "Hulk", "attack_power": 300, "life": 1000}

# Super Villains
THANOS = {"name": "Thanos", "attack_power": 400, "life": 1800}
REDSKULL = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA = {"name": "Proxima", "attack_power": 320, "life": 800}

# All Super Heros & Super Villains
superheros = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
villains = [THANOS, REDSKULL, PROXIMA]

# all super heros and super villans 
super_heroes = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]

super_villians = [THANOS, REDSKULL, PROXIMA]

hero_life: int = 0
villians_life: int = 0

# declare helper messages 
WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

#attack 
for attack in range(3):
  #each iteration get a new hero & villans
  hero_index = randint(0,len(super_heroes)-1)
  villian_index = randint(0,len(super_villians)-1)
  
  #helper variables
  current_super_hero = super_heroes[hero_index]
  current_super_villian = super_villians[villian_index]
  
  #life
  hero_life += hero_life + current_super_hero['life']
  villians_life += villians_life + current_super_villian['life']

  #attack
  hero_life -= current_super_hero['attack_power']
 
  villians_life -= current_super_villian['attack_power']
  

  #output
  print(f"Attack: {attack} => {current_super_hero['name']} is going to fight with {current_super_villian['name']}")
  print(f"the hero still has life: {hero_life}")
  print(f"the villian still has life: {villians_life}")
   
#print a nice separatin line
print("=" * 70)

#win of loose 
if hero_life >= villians_life:
  print(WIN_MSG)
else:
  print(LOST_MSG)