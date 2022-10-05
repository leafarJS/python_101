#while traveling to Zortan, jorge packed lost of stuff, Let's see if he has anything that matches your favorite color 

#mientras viajaba a Zortan, jorge empacó cosas perdidas, a ver si tiene algo que coincida con tu color favorito

"""
INFO -
------
`match` is a new operator introduced in Python 3.10
"""

fav_color: str = input("Enter your favorite color: ").lower()

match fav_color:
    case "black":
        print("Louis has a BLACK T-Shirt.")
    case "red":
        print("Louis has a RED car.")
    case "yellow":
        print("Louis has YELLOW shoes.")
    case "green":
        print("Louis has a GREEN hat")
    case _:
        print(f"Louis has nothing in {fav_color} color.")
    