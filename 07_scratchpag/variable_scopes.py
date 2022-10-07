"""
Variable Scope:
---------------
Scopes can be `Global` or `Local`
"""
""" 
Alcance variable:
---------------
El alcance puede ser "Global" o "Local".
"""
#global
num = 10

def print_global_num():
  print(f"global num is {num}")
  

def print_num():
  #function or local scope
  num = 20
  print(f"local num is {num}")
  
def inc_num():
  #explicit global declaration
  global num
  num += 2
  
def inc_local_num():
  new_num = num +10
  print(new_num)


print_global_num()
print_num()
inc_num()
print(num)
inc_local_num()

