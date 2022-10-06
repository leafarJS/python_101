"""
Functions:
----------
Think in data transformations -
`take something -> give something`
Delegate handling responsibility to the caller function.
Tip:
-----
Very useful pattern for testing!!!
"""

""" 
Piense en las transformaciones de datos -
`tomar algo -> dar algo`
Delegue la responsabilidad de manejo a la función de llamada.
Consejo:
-----
Patrón muy útil para probar!!!
"""

#returns a greetting message to caller functions
#caller function decides what to do with the response
def greeter(name: str) -> str:
  #Greeter 'transforms' original string to something useful
  #and return it.
  return f"Zola {name}"
  

def main()-> None:
  friends: list[str] = ["caca", "cece", "cici", "coco", "cucu"]
  for f in friends:
    #main acts as the 'caller function' for greeter.
    #it can handle response in multiple ways
    if "cucu" in greeter(f):
      print(f"{f} is agly")
    else:
      print(greeter(f))

#invoke  the main function 
main()