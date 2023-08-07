print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
wait_or_swim = input(
    "You arrive at a dock after running from the bandits, you can wait for a boat, but you can hear them coming! Swim or Wait?\n"
)
wait_or_swim = wait_or_swim.lower()

if wait_or_swim == "swim":
    print(
        "You start to swim away, you can see the island in the distance as the sharks finish you off"
    )
elif wait_or_swim == "wait":
    print(
        "You wait for the boat, the approaching footsteps turn out to be a drunk couple! You sail to the island safely"
    )
    left_or_right = input(
        "You arrive at the island, you cant see as you're greeted by a cliff. You have two options, Left you can see a dim light in the distance, or Right where you can see a bird in its nest. Left or Right?\n"
    )
    left_or_right = left_or_right.lower()
    if left_or_right == "right":
        print(
            "You head towards the bird, as you get closer the bird flys at you causing you to fall to your death."
        )
    elif left_or_right == "left":
        open_or_dig = input(
            "You head towards the dim light, you stumble in the darkness but regain your balance. You arrive at a door. On the floor next to it is a half dug grave. What do you do? Open or Dig\n"
        )
        open_or_dig = open_or_dig.lower()
        if open_or_dig == "open":
            print(
                "You push open the door, behind it is a hideous creature that decapitates you in seconds. Game over"
            )
        elif open_or_dig == "dig":
            print(
                "You start to dig and hear a massive bang. Something is trying to come through the door, you continue to dig and that's when you see it. All the treasure you could dream of. The One Piece! Well done!"
            )
