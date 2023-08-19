import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

word_length = len(chosen_word)


database = []
for word in range(word_length):
    database += "_"


lives = 6
import os

def clear_terminal():
    os.system('cls')
print(logo)
print("Welcome to Hangman game")

end_of_game = False

while end_of_game == False:
    
    while True:
      guess = input("Guess a letter: ").lower()
      if len(guess) == 1 and guess.isalpha():
        break
      else:
        clear_terminal()
        print("Invalid input. Please enter a letter.")
    
   
    if guess in database:
        print("You already guessed that letter")
        print(database)
    

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            database[position] = letter
            clear_terminal()
            print(database)
    
    if guess not in database:
        lives-=1
        clear_terminal()
        print(f"You guessed incorrectly and you have lost a life you have {lives} left")
        print(stages[lives])
        print(database)
        
    if lives == 0:
        print("You have 0 life left")
        print("Game over")
        print(stages[lives])
        end_of_game = True
    if "_" not in database:
        print("You Win!")
        print(logo)
        end_of_game = True
