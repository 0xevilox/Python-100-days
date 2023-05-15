# 🚨 Don't change the code below 👇
row1 = ["😊","️😊","️😊","😊"]
row2 = ["😊","😊","️😊","😊"]
row3 = ["😊️","😊","😊","😊"]
row4 = ["😊️","😊","😊","😊"]
map = [row1, row2, row3,row4]   # Nested List
print(f"{row1}\n{row2}\n{row3}\n{row4}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

coloum = int(position[0]) - 1
row = int(position[1]) - 1

select = map[row]
select[coloum] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}\n{row4}")
