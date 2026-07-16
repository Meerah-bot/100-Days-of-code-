print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!!")
print("Your mission is to find the treasure.")
path=input("You're in a tunnel, you need to choose a path.left or right: \n")

if path == "left":
    print("You've fallen into a river")
    if path =="right":
        print("You've been captured.Game over")
    second_path = input("swim over or  wait for a boat:\n").lower()
    if second_path == "swim":
        print("You've drowned, Game over.")
    elif second_path =="wait":
        third_path = input("Which boat would you like to ride on? Red, Yellow ,Blue:\n").lower()
        #This can be used instead of double quotes("")
        #and if there is you have word(it can be written like you\'ve with the backslash character)
        if  third_path == "red" and "blue":
         print("Your boat's been hijacked by pirates, Game over.")
        if  third_path == "yellow" :
         print("Congratulations you have won!!!")
        else:
         print("You have entered an invalid path.")

else:
    print("You have entered an invalid path.")
