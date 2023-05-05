print( '''
                        __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \\
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \\
      .'`   `\\            | |                \\
     /        |           | |                 ;
     |        /           |_|                 |
     \\  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\\      | |_ | | || |/ /|  _|   .' `,
           `\\    |___|\\___/ \\__/ |___|  |     \\
             \\            _ _           \\     |
         jgs  `\\         | | |         /`   _/
    ,-""-.    .'`\\       | | |       /`-,-'` .-""-,
   /      `\\.'    `\\     \\___/     /`    './`      \\
  ;  .--.   \\       '\\           /'       /   .--.  ;
  | (    \\   |,       '\\       /'        |   /    ) |
   \\ ;    }             ;\\   /;         `   {    ; /
    `;\\   \\         _.-'  \\ /  `-._         /   /;`
      \\ \\__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'
''')

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
var = name1.lower()
var_1 = name2.lower()
name = (var+var_1)
count = name.count('t')
count_1 = name.count('r')
count_2 = name.count('u')
count_3 = name.count('e')
result = count + count_1 + count_2 + count_3
count_8 = name.count('l')
count_9 = name.count('o')
count_10 = name.count('v')
count_11 = name.count('e')
result_1 = count_8 + count_9 + count_10 + count_11
completed_love = str(result) + str(result_1)
var_2 = int(completed_love)
if var_2 <= 10 or var_2 >=90:
        print(f"Your score is {var_2}, you go together like coke and mentos.")
elif 40 <= var_2 <= 50:
    print(f"Your score is {var_2}, you are alright together.")
else:
    print(f"Your score is {var_2}")
