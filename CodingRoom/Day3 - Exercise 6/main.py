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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

FirstQuestion = "You're at a cross road. Where do you want to go? \n Type \"left\" or \"right\". "
FirstAnswer = input(FirstQuestion)
SecondQuestionLeft = "\n ~~~ \n ~~~ \n ~~~ \nYou're get into lake. you have to cross the lake. Do you want to wait boat comming or you want to  swim? \n Type \"wait\" or \"swim\". "
SecondQuestionRight = "You fell into a hole. "
SecondAnswer = input(SecondQuestionLeft)
ThirdQuestionWait = ("\n Finally you get in to rainbow gate. Wich door do you want to open? \n Type \"red\", \"blue\" or \"yellow\". ")
ThirdQuestionSwim = ("You get bite by aligator. ")
ThirdAnswer = input(ThirdQuestionWait)
FourthQuestionYellow = "\n You did it, you get the crown and medal. "
FourthQuestionRed = "You get attack by Bear. "
FourthQuestionBlue = "You get attack by Rabbit. "

GameOver = "Game Over."
Win = "You win"

print(FirstAnswer)
if FirstAnswer == "left":
    print(SecondQuestionLeft)
    if SecondAnswer == "wait":
        print(ThirdQuestionWait)
        if ThirdAnswer == "yellow":
            print(FourthQuestionYellow, Win)
        elif ThirdAnswer == "blue":
            print(FourthQuestionBlue, GameOver)
        elif ThirdAnswer == "red":
            print(FourthQuestionRed, GameOver)
    elif SecondAnswer == "swim":
        print(ThirdQuestionSwim, GameOver)
elif FirstAnswer == "right":
    print(SecondQuestionRight, GameOver)
    