
# jorge wants to drive a car 🚗 and wants to know if he can apply for a driving license or not

#jorge quiere conducir un auto 🚗 y quiere saber si puede solicitar una licencia de conducir o no

age: int = 13

# if / else Statement 

if age < 16:
  print('You are NOT eligible for a license')
else:
  print("You are eligible for a driving license")
  
# after a couple of year

age = 19

if age < 16:
  print('You are NOT eligible for a license')
else:
  print("You are eligible for a driving license")
  
#alternative implementation -without 'else' block

  age = 21

  if age < 16:
    print('You are NOT eligible for a license')
      

print("You are eligible for a driving license")
  

# after too many years

age = 100

if age < 16:
  print('You are NOT eligible for a license')
elif age > 100:
  print("You are too old to get a license.")
else:
  print("You are eligible for a driving license")
