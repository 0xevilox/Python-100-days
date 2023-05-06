# 🚨 Don't change the code below 👇
row1 = ["😊","️😊","️😊","😊"]
row2 = ["😊","😊","️😊","😊"]
row3 = ["😊️","😊","😊","😊"]
row4 = ["😊️","😊","😊","😊"]
map = [row1, row2, row3,row4]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
var = int((position[0])) - 1
var_1 = int((position[1])) - 1

selected = map[var_1]
selected[var] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
