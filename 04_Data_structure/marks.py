#Diccionary

#jorge has given his exams and received marks. Let's check out how did he fare

#dicionary makes it easy to have key - value pairs

#jorge ha dado sus exámenes y ha recibido notas. Veamos cómo le fue

#dicionario hace que sea fácil tener pares clave - valor

marks:dict[str, int] = {
  "Maths": 80,
  "Science": 60,
  "History": 50,
  "English": 35,
  "Python": 90,
  "Physics": 18
}

print(f"Marks: {marks}")

# jorge wants to check out all the subjects {keys}

for k in marks.keys():
  print(k)
  
  # jorge wants to check out all the subjects {value}
  
for v in marks.values():
  print(v)
  
#jorge wants to check out all the subjects & marks together {key-value}

for k, v in marks.items():
  print(f"{k}: {v}/100")
  
#jorge wants to check if he passed all of the subjects, Passing mark 50

for k, v in marks.items():
  if v >= 50:
    print(f"{k}, PASS")
  else:
    print(f"{k} FALIED!!")

#Jorge request revaluation of this English paper, there was a totalling mistake and right mark are 70

marks["English"] = 70
print(f"jorge scored {marks['English']} in English")

# jorge also took Physics and scored 78

marks["Physics"] = 78
print(f"jorge scored {marks['Physics']} in English")
#jorge again wants to check if he passed in all of the subjects

for k, v in marks.items():
  if v >= 50:
    print(f"{k}, PASS")
  else:
    print(f"{k} FALIED!!")
    
# friends on Zortan want's to know how much jorge scored in Python

#opcion A
python_score = marks["Python"]
print(f"Jorge scored {python_score} in python")

#opcion B
python_score = marks.get("Python")
print(f"Jorge scored {python_score} in python")

#friends on Earth want's  to know how much jorge scored Java

#option A
#! will throw error
""" java_score = marks["Java"]
python_score = marks.get("Python")
print(f"Jorge scored {python_score} in java") """

#option B
java_score = marks.get("Java")
if java_score is None:
  print("jorge did not study Java")
else:
  print(f"Jorge scored {java_score} in java")
  
  #Deleting an element from dictionary
  
  del marks["English"]
  print(f"Marks: {marks}")
  
  