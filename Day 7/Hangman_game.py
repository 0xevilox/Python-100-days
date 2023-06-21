print('''
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                     ''')
stage = [
    '''  +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''',
    '''  +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''',
    '''  +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''',
    '''  +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''  +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''  +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''  +---+
      |   |
          |
          |
          |
          |
    ========='''
]
#random module
import random
#This wordlist to guess
word_list = open("D:/Programming/hangman.txt")
#make the random word
word_list = word_list.read().splitlines()
chosen_word = random.choice(word_list)
#Counting the length
measure = len(chosen_word)
#Count of the life
live = 7
# print(f'Pssst, the solution is {chosen_word}.')
#Setting the boolean for while loop to start
end_game = False
display = []
for blank in range(0, measure):
    display += "_"
while not end_game:
    print("Movie Mind Teaser: Can You Guess the Movie Name?")
    user = input("Enter a letter to Guess: ").lower()
    for position in range(measure):
        guess = chosen_word[position]
        if guess == user:
            display[position] = guess
    print(display)
    if "_" not in display:
        #setting the boolean for while loop to stop
        end_game = True
        print("You Win")
    if user not in chosen_word:
        live -= 1
        if live == 0:
            end_game = True
            print("You Lose")
            print(chosen_word)
        print(stage[live])
