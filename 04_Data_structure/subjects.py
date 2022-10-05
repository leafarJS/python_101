# Tuple:
# Time for jorge to go to school, and its time for him choose subjects. School doesn's want students to change subjects after they are chosen, so they use Tuple.

#tuple is like a stricter brother of List. Once a tuple is created, it cannot be edited. 

# Tupla:
# Es hora de que jorge vaya a la escuela, y es hora de que escoja materias. La escuela no quiere que los estudiantes cambien de tema después de haberlos elegido, por lo que usan Tuple.

#tuple es como un hermano más estricto de List. Una vez que se crea una tupla, no se puede editar.

#asignaturas
#subjects:tuple[str, str, str, int] = ("Maths", "Science", "History", 13)
subjects:tuple[str, str, str] = ("Maths", "Science", "History")

#jorge wants to count his subjects

print(f"Number of subjects: {len(subjects)}")

# jorge needs to singup for all the subjects 

for subject in subjects:
  print(f"jorge is singing up for : {subject}")
  
#jorge wants to see which is his second subject

print(subjects[1])

#school wants jorge to take another 3 subjects to get full credits 

addl_subject:tuple[str, str, str] = ("English", "Python", "Physics")
total_subjects = subjects + addl_subject
print(f"All my subjects: {total_subjects}")

#jorge loves Python, and wants to see if it's there in his subjects

if "Python" in total_subjects:
  print("Oh-yeah, jorge is going to learn Python")
else:
  print("ondy sheet!!")