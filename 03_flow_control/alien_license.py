# jorge wants to drive a car πΊ and he hears that in planet Zortan πͺ there is no age limit for getting a license.


#jorge quiere manejar un carro πΊ   y escucha que en el planeta Zortan  πͺ  no hay lΓ­mite de edad para sacar la licencia.

age: int = 13
planet: str = "Earth"

# And / Or statement

if age < 16 and planet == "Earth":
  print("You are NOT eligible for license on Earth π")
  
elif age > 16 and planet == "Earth":
  print("You can apply for license on Earth π")
  
elif age < 16 and planet == "Zortan":
  print("You can apply for Zortanian πͺ license!!")
  
else:
  print("You are not from this planet and you are not of the required age")


#pip install ipython
#ctrl + d  = exit
# "AND TABLE"

""" 
In [1]: True and True
Out[1]: True

In [2]: False and False
Out[2]: False

In [3]: True and False
Out[3]: False

In [4]: False and True
Out[4]: False
"""

# "OR TABLE"

"""
In [5]: True or True
Out[5]: True

In [6]: False or False
Out[6]: False

In [7]: True or False
Out[7]: True

In [8]: False or True
Out[8]: True

"""


# Jorge migrantes to Zortan
age = 21
planet = "Zortan"

if age < 16 and planet == "Earth":
  print("You are NOT eligible for license on Earth π")
  
elif age > 16 and planet == "Earth":
  print("You can apply for license on Earth π")
  
elif age < 16 and planet == "Zortan":
  print("You can apply for Zortanian πͺ license!!")

elif age > 16 and planet == "Zortan":
  print("You can apply for license on Zortan πͺ")  
else:
  print("You are not from this planet and you are not of the required age")