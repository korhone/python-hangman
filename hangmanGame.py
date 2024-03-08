import random
import sys
lives = 0
heart = u'\u2764\uFE0F'
guessed_word_right = False
clue = [] 
index = 0 

# Vaikeustason valinta
def difficulty(): 
    try:
        userinput_difficulty = int(input("Choose a difficulty level (enter 1, 2 or 3): \n 1. Easy\n 2. Normal\n 3. Hard\nYour choice: "))
        if userinput_difficulty == 1:
            lives = 9
            return lives
        if userinput_difficulty == 2:
            lives = 6
            return lives
        if userinput_difficulty == 3:
            lives = 3
            return lives
        else:
            print("Only use numbers 1, 2 or 3! Please select your difficulty level again: ")
            lives = difficulty()
            return lives
    except: 
        print("You cannot select the difficulty level with letters, try again with numbers: ")
        lives = difficulty()
        return lives

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters -= 1
        index += 1
    return unknown_letters

# salaisten sanojen nouto tekstitiedostosta ja pelin arvattavan sanan määritys:
try:
    filename = "YOUR_FILE_NAME.txt"
    file = open(filename, "r")
    words_inlist = file.readlines()
    file.close()
    secret_word = random.choice(words_inlist).upper()
    secret_word = secret_word.strip("\n")
    unknown_letters = len(secret_word)
    
    while index < len(secret_word):
        clue.append("?")
        index += 1
except:
    print(f"File {filename} not found, check the filename.")
    sys.exit(1)
    
#Silmukka joka kyselee kokoajan kirjainta kunnes arvataan oikein tai elämät loppuvat

lives = difficulty()

try:
    while lives > 0:
        print(', '.join(clue))
        print("Lives left:", ' '.join(heart * lives))
        guess = input("Guess the letter or the whole word: ").upper()

        if guess == secret_word:
            guessed_word_right = True
            break
        if guess in secret_word:
            unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        else:
            print("Wrong. You lost one life \n")
            lives -= 1
        if unknown_letters == 0:
            guessed_word_right = True
            break
    if guessed_word_right:
        print("\n You won! The secret word was:", secret_word , "\n")
    else:
        print("\n You lost! The secret word was:", secret_word, "\n")
except:
    print("An error occurred, please contact the coder of the game.")
