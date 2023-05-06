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

images = [rock,paper,scissors]
import random
print("Welcome to Rock,Paper and Scissors")
user_2 = input("Enter your name: ")
print("Now your going to fight with a Computer bot")
user = int(input("What do you choose? Type 0 for Rock, 1 for a paper or 2 for Scissors \n"))
user_1 = images[user]
print(f"{user_2} has choose {user} ",user_1)
rand = random.randint(0,2)
user_3 = images[rand]
print(f"Bot has choose {rand} ", user_3)
if user == rand:
    print("The game draw")
elif user == 0 and rand ==2:
    print("You win the game!!")
elif user == 2 and rand ==0:
    print("Computer win the game!!")
elif user == 2 and rand ==1:
    print("You win the game!!")
elif user == 1 and rand == 2:
    print("Computer win the game!!")
elif user == 1 and rand == 0:
    print("You win the game!!")
elif user == 0 and rand == 1:
    print("Computer win the game!!")
else:
    print("You entered Invalid Number")
