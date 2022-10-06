class Character:
  def __init__(self, name:str, attack_power:int, life:int) -> None:
    #creates an instances of 'Character'
    self.name = name
    self.attack_power = attack_power
    self.life = life
    
  def __repr__(self) -> str:
    return "<class 'Character'>"
  
  def __str__(self) -> str:
    return f"Name: {self.name}, Attack Power {self.attack_power}, Life {self.life}"
  

villian_one = Character("Thanos", 400, 1500)
#using key value pairs
villian_two = Character(name="Redskull", life = 800, attack_power = 400)

hero_one = Character(name="Ironman", attack_power = 450, life = 800)
hero_two = Character(name="BlackWidow", attack_power = 150, life = 700)

print(villian_one)
print(villian_two)

print(hero_one)
print(hero_two)