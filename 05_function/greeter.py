"""
Functions:
----------
It's all about data transformation, ideally it should:
`take something -> give something`
Or else, it causes a `side effect`.
Remember people in Zortan greet each other by saying Zola,
jorge wants to write a program which can greet any Zortan!
"""
""" 
Se trata de la transformación de datos, idealmente debería:
`tomar algo -> dar algo`
O bien, provoca un 'efecto secundario'.
Recuerda que la gente en Zortan se saluda diciendo Zola,
¡jorge quiere escribir un programa que pueda saludar a cualquier Zortan!
"""
def greeter(name) -> None:
  #Greets Zortan 
  print(f"Zola {name}")
  

def main()-> None:
  friends: list[str] = ["caca", "cece", "cici", "coco", "cucu"]
  for f in friends:
    greeter(f)
    
#invoke  the main function 
main()
    

