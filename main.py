import random
from hangman_logo import logo
from hangman_stages import stages
from word_list import word_list

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
print(logo)
print("Welcome to the Hangman Game 🤗")
print("You will need to guess the word, one letter at a time")
print("If your guess is incorrect you lose a life")
print("You only have 6 lives to make incorrect guesses. Have fun!")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_end = False
lives = 6

display = ["_"] * word_length

print(f'Solution is {chosen_word}.')

while not game_end:
    print(f"\nCurrent word: {' '.join(display)}")
    print(stages[lives])

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or guess not in ALPHABETS:
        print("Invalid input. Please enter a single letter.\n")
        continue

    if guess in display:
        print(f"You have already guessed the letter '{guess}'")
        continue

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You chose '{guess}', which is not in the word. You lose a life ☠️.")
        lives -= 1
        if lives == 0:
            game_end = True
            print(f"You lose. The word was '{chosen_word}' 🤕. Better Luck next time!")
            break

    if "_" not in display:
        game_end = True
        print(f"Congratulations! You've guessed the word '{chosen_word}' correctly. YOU WON! 🎉")

print(stages[lives])
