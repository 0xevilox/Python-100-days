# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Without choice function
var = len(names)
rand_choice = random.randint(0,var)
who_pay = (names[rand_choice])
print(f"{who_pay} is going to buy the meal today!")

# With choice function

rand_choice_1 = random.choice(names)
print(f"{rand_choice_1} is going to buy the meal today!")
