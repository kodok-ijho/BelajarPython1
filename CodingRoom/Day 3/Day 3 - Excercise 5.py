# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#name1Lower = name1.lower()
#name2Lower = name2.lower()
nameLower = name1.lower() + name2.lower()

countTrue = 0
countLove = 0

countTrue = countTrue + nameLower.count("t")
countTrue = countTrue + nameLower.count("r")
countTrue = countTrue + nameLower.count("u")
countTrue = countTrue + nameLower.count("e")

countLove = countLove + nameLower.count("l")
countLove = countLove + nameLower.count("o")
countLove = countLove + nameLower.count("v")
countLove = countLove + nameLower.count("e")

Total = (countTrue * 10) + countLove

if Total < 10 or Total > 90:
    print(f"Your score is {Total}, you go together like coke and mentos.")
elif Total > 40 and Total < 50:
    print(f"Your score is {Total}, you are alright together.")
else:
    print(f"Your score is {Total}.")