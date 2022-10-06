"""
Class can have class variables as well as instance variables.
Class variables are shared across all instances while instance variable are only limited to that particular instance.
"""
""" 
La clase puede tener clases variables así como variables de instancia.
Las variables de clase se comparten entre todas las instancias, mientras que la instancia
variable solo se limitan a esa instancia en particular. 
"""
class Box:
  
  #class variable /members
  box_type = "Packaging Carton"
  color = "Brown"
  
  def __init__(self, side_a:int, side_b:int) ->None:
    #Instance variables/members
    self.side_a = side_a
    self.side_b = side_b

def __str__(self) -> str:
  return f"Side A: {self.side_a}, side B: {self.side_b}"

box_one = Box(3,4)

print(box_one)
print(box_one.color)
print(box_one.box_type)

#not needs create instances with this class
print(Box.color)
print(Box.box_type)

box_two = Box(10,100)
print(box_two)
print(box_two.color)
print(box_two.box_type)
