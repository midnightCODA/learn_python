import sys
import random
from enum import Enum

class Arsenal_TopPlayers(Enum):
    LEFT_WING_STARTER = "MARTINELLI"
    RIGHT_WING_STARTER = "SAKA"
    CENTER_FORWARD_STARTER = "GABRIEL JESUS"

# container = input("enter something but there isno a trailing line? \n")

# print("So you have comepleted yur user input \n\n")

# print(container)
# print(type(container))

# so turns out when ever we use an input we get a string
# if we want a number we need to con vert it to a number


# RANDOM CHOICE

# selectRandomNumber = input("enter a random number?")

# if selectRandomNumber == '':
#     sys.exit('Failed you must put a random number')

# playerchoice = int(selectRandomNumber)

# randomresult = random.choice("12345")



# print('Your choice is ' + str(playerchoice))
# print('The computers choice ' + randomresult )



print(Arsenal_TopPlayers.CENTER_FORWARD_STARTER.value)



#  what are enums in python and how are they used?


