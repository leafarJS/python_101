""" 
Zortan is under attack!! Thanos has arrived!
-------------------------------------------- 


Since Zortan is under attack, jorge calls his Avenger friends from Earth, Avengers receive his call and sends 4 avengers to save Zortan

1. Ironman
2. Black Widow
3. Spiderman
4. Hulk

Each avenger has its attacking power and they have to fight Thanos to save Zortan

Avengers can attack only in pairs and get only 3 chance to kill Thanos, or else Thanos will kill avengers and we loose the game.
"""
from typing import Final

# ! Un construcción especial para tipado que indica a los validadores de tipo que un nombre no puede ser reasignado o sobrescrito en una subclase.
IRONMAN_ATTACK_POWER: Final[int] = 250
BLACK_WIDOW_ATTACK_POWER: Final[int] = 150
SPIDERMAN_ATTACK_POWER: Final[int] = 200
HULK_ATTACK_POWER: Final[int] = 350

thanos_life: int = 1500
choise:int = 0
attack_num: int = 0

# declare helper messages 
WIN_MSG: Final[str] = "You successfully saved Zortan!!! 🪐✨✨✨🪐🌏✨✨✨✨🎉🥇🎯"

LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!!! 💀☠💀👻👽🦴🦴🏴‍☠️🏴‍☠️ "

MSG: Final[str] = """
-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
Zartan is under attack, choose the pairs No.
that will attack Thanos

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman

-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
"""
print(MSG) 

while True:
      # win or lose for exit loop 
  if thanos_life <= 0 and attack_num <= 3:
    print(WIN_MSG)
    break 
  elif attack_num >= 3:
    print(LOST_MSG)
    break
        
  choise = int(input("Enter your pair heroes from 1 al 4: >>>"))
        
  
  if choise == 1:
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    print("Ironman & Black Widow are attacking Thanos...")
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    thanos_life = thanos_life - (IRONMAN_ATTACK_POWER + BLACK_WIDOW_ATTACK_POWER)
    print(f"Thanos have a power of : {thanos_life}")
    attack_num = attack_num + 1
  elif choise == 2:
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    print("Black Widow & Spiderman are attacking Thanos...")
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    thanos_life = thanos_life - (BLACK_WIDOW_ATTACK_POWER + SPIDERMAN_ATTACK_POWER)
    print(f"Thanos have a power of : {thanos_life}")
    attack_num = attack_num + 1
  elif choise == 3:
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    print("Spiderman & Hulk are attacking Thanos...")
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    thanos_life = thanos_life - (SPIDERMAN_ATTACK_POWER + HULK_ATTACK_POWER)
    print(f"Thanos have a power of : {thanos_life}")
    attack_num = attack_num + 1
  elif choise == 4:
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    print("Hulk & Ironman are attacking Thanos...")
    print("🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡⚔🏹🗡")
    thanos_life = thanos_life - (HULK_ATTACK_POWER + IRONMAN_ATTACK_POWER)
    print(f"Thanos have a power of : {thanos_life}")
    attack_num = attack_num + 1
  else:
    print("This pair is NOT correct and NOT exist!!!")