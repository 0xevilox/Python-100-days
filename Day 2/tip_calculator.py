#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

user = float(input("Enter the amount to split:"))
percentage = float(input("what percentage would give 10%,12% or 15%:"))
people = float(input("How much people you want to split:"))
div =  user * percentage / 100 
total = user + div
split = total / people 
formatted_split = "{:.2f}".format(split)

print("Each person should pay:" + formatted_split)