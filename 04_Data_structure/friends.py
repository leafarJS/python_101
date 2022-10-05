"""
List:
-----
jorge has been making good progress in Zortan and has made new friends. All of them are meeting today and jorge wants to write a program that can greet all of them. In Zortan, people greet with saying "Zola"
Info:
-----
Lists are mutable data structures, that means the data inside can be mutated.
Index always starts from 0.
"""
"""
jorge ha progresado mucho en Zortan y ha hecho nuevos amigos. Todos ellos se encuentran hoy y jorge quiere escribir un programa que pueda saludarlos a todos. En Zortan, la gente saluda diciendo "Zola".
Información:
-----
Las listas son estructuras de datos mutables, lo que significa que los datos que contienen se pueden mutar.
El índice siempre comienza desde 0.
"""

#it.s convenient to group all friends together using a 'list' adn them great them

#length               [  1       2       3      4   ]
friends: list[str] = ["cece", "coco", "caca", "cucu"] # value | str | int | float | dic |
#index               [  0       1       2      3   ]

# time to greet friends using a for in loop

for friend in friends:
  print(f"Zola, {friend}")
  
# jorge wants to count his number of friends 

print(f"Friends length: {len(friends)}")

# jorge had a fight with cucu and wants to unfriend him (jorge se peleó con cucu y quiere quitarlo de su amistad)

unfriend = friends.pop()
print(f"Unfriend: {unfriend}")
print(f"Friend {friends}")


# jorge makes a new friend cici 

friends.append("cici")
print(f"Friend {friends}")

# jorge wants to check who is 3ra in this friend list

print(friends[2]) #remember since list starts from index 0 we use number - one


# OH-no jorge again had a fight, this tiem whit coco

friends.remove('coco')
print(f"Friend {friends}")

#jorge and coco become friends again!

friends.insert(1, "coco")
print(f"Friend {friends}")

# jorge wants to confirm  if coco is in friends list

friend = "coci"
if friend in friends:
  print(friends)
else:
  print(f"{friend} is NOT your friend!!!")


# jorge patches up with cici as well and he become his No. 1 friend (jorge también se arregla con cici y se convierte en su amigo número 1)

friends.insert(0, "cici")
print(f"Friend {friends}")

# jorge wants changing one friends cici

friends[3] = "cucu"
friends[2] = "caca"
print(f"Friend {friends}")


# jorge wants to sort his friends in alphabetical order

friends.sort()
print(f"Friend {friends}")

# No, jorge doesn't like this ordering and wants to reverse the order 

friends.reverse()
print(f"Friend {friends}")

# what's this! jorge again had a fight with cici

unfriend = friends.pop(1)
print(f"Unfriend: {unfriend}")
print(f"Friend {friends}")


#jorge and coco become friends again!

friends.insert(len(friends) - 1, "coco")
print(f"Friend {friends}")

# jorge wants again to sort his friends in alphabetical order

friends.sort()
print(f"Friend {friends}")


