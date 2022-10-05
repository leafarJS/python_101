# friends from Earth 🌎 want to know were is jorge, so jorge decides to write a program that will make his friends guess the of planet

#amigos de la Tierra 🌎 quieren saber donde esta jorge, entonces jorge decide escribir un programa que haga que sus amigos adivinen el planeta

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

#alternative 1

#ctrl + , code runner  ✔ Code-runner: Run in Terminal

while correct_guess is not True:
  guess = input("Jorge says: Can you guess my planet?>>>")
  if guess.lower() == planet.lower():
    print("Right guess!!, Jorge is at Zortan")
    correct_guess = True
  else:
    print("Wrong Choise, try again!")
    print("________________________")

#alternative 1

while True:
  guess = input("Jorge says: Can you guess my planet?>>>")
  if guess.lower() == planet.lower():
    print("Right guess!!, Jorge is at Zortan")
    break
  else:
    print("Wrong Choise, try again!")
    print("________________________")
    print()

