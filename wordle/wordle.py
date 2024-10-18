from words import words_list
from random import choice
from colorama import *

#word that has to be guessed
chosen_word = choice(words_list)

#attempts left
tries_left = 6 
guess = ""

#game loop
while tries_left > 0 and chosen_word != guess:
    print("attempts: " + str(tries_left))
    guess = input("Guess the five letter word: ")
    #checking if player guess is valid 
    if len(guess) != 5 or guess not in words_list:
        print("invalid word")
        continue
    #comparing the characters of the chosen word and player guess
    if chosen_word[0] == guess[0]:
        print(Fore.GREEN + guess[0], end="")
    elif guess[0] in chosen_word:
        print(Fore.YELLOW + guess[0], end="")
    else:
        print(guess[0], end="")
    if chosen_word[1] == guess[1]:
        print(Fore.GREEN + guess[1], end="")
    elif guess[1] in chosen_word:
        print(Fore.YELLOW + guess[1], end="")
    else:
        print(Style.RESET_ALL + guess[1], end="")
    if chosen_word[2] == guess[2]:
        print(Fore.GREEN + guess[2], end="")
    elif guess[2] in chosen_word:
        print(Fore.YELLOW + guess[2], end="")
    else:
        print(Style.RESET_ALL + guess[2], end="")
    if chosen_word[3] == guess[3]:
        print(Fore.GREEN + guess[3], end="")
    elif guess[3] in chosen_word:
        print(Fore.YELLOW + guess[3], end="")
    else:
        print(Style.RESET_ALL + guess[3], end="")
    if chosen_word[4] == guess[4]:
        print(Fore.GREEN + guess[4] + Style.RESET_ALL)     
    elif guess[4] in chosen_word:
        print(Fore.YELLOW + guess[4] + Style.RESET_ALL)
    else:
        print(Style.RESET_ALL + guess[4]) 
    #subtracting attempts 
    tries_left -= 1 
    #ending the game
    if chosen_word == guess:
        print("You win!")
    elif tries_left == 0:
        print(f"Game over, the word was {chosen_word}")



