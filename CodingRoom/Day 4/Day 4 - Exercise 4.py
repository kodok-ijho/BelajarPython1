# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list_games = [rock,paper,scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(list_games[human_choice])

computer_choice = random.randint(0, 2)
print(f"Computer choose: \n {list_games[computer_choice]}")

result = 0

# Human Win
if human_choice == 0 and computer_choice == 2:
    result = 1
if human_choice == 1 and computer_choice == 0:
    result = 1
if human_choice == 2 and computer_choice == 1:
    result = 1

# Human Lose
if human_choice == 0 and computer_choice == 1:
    result = 2
if human_choice == 1 and computer_choice == 2:
    result = 2
if human_choice == 2 and computer_choice == 0:
    result = 2

if result == 0:
    print("Draw")
elif result == 1:
    print("You win")
else:
    print("You lose")

