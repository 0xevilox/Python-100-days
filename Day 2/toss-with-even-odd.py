import random
import time
print("Welcome to HandCricket First let's put the toss")
Name = input("Enter the You Name: ")
Ask_User = input("Enter odd or even: ")# Getting the input odd or even
low = Ask_User.lower() #conver lower
if low == "odd": # if equal to odd
    print(f"{Name} is chosen: {Ask_User}")
    print("Computer is chosen even")
    li = [1, 2, 3, 4, 5, 6]  # Getting random number from computer
    computer = random.choice(li)
    User = int(input("Enter the Number with range of 1 to 6: "))
    print(f"Your Number is: {User}")
    print(f"Computer Number is: {computer}")
    add_total = computer + User
    if User > 6:
        print("Don't do this supid things to my Game.Enter the Number with range of 1 to 6 only")
    elif add_total % 2 == 0:
        to = "even"
        if low == to:
            print(f"{Name} has Win the toss because it's {Ask_User}")
        else:
            print("Computer Win the toss because it's even")
    else:
        op = "odd"
        if low == op:
            print(f"{Name} has Win the toss because it's {Ask_User}")
        else:
            print("Computer Win the toss because it's odd")
    time.sleep(2)
    print("Now the Toss Completed.........")
    time.sleep(2)
    print("Now the Toss Completed..........")
elif low != "odd" and low != "even": # If some cause error
    print("Don't do this supid things to my Game. Chose odd or even only and Restart the Game")
else:
    print(f"{Name} is chosen: {Ask_User}")
    print("Computer is chosen odd")
    li = [1, 2, 3, 4, 5, 6]  # Getting random number from computer
    computer = random.choice(li)
    User = int(input("Enter the Number with range of 1 to 6: "))
    print(f"Your Number is: {User}")
    print(f"Computer Number is: {computer}")
    add_total = computer + User
    if User > 6:
        print("Don't do this supid things to my Game.Enter the Number with range of 1 to 6 only")
    elif add_total % 2 == 0:
        to = "even"
        if low == to:
            print(f"{Name} has Win the toss because it's {Ask_User}")
        else:
            print("Computer Win the toss because it's even")
    else:
        op = "odd"
        if low == op:
            print(f"{Name} has Win the toss because it's {Ask_User}")
        else:
            print("Computer Win the toss because it's odd")
    time.sleep(2)
    print("Now the Toss Completed.........")
    time.sleep(2)
    print("Now the Toss Completed...........")
