import random
import string
def hangman():
    words = ['sathish','santhosh','basavanna','latha']
    word = random.choice(words)
   
    word_letters = set(word) # convert the word to characters
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 5
    while len(word_letters) > 0 and lives > 0:
        print(f"you have {lives} lives left and you have used these: {' '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word is : ',''.join(word_list))
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"your letter {user_letter} is not present in the word selected")
        elif user_letter in used_letters:
            print("you have already guessed this letter, please choose other one")
        else:
            print('Invalid character, please enter again')

    if lives == 0:
        print(f'Sorry, you have lost the game the word was {word}')
    else:
        print(f"super,you have guessed word correct, the word was '{word}'")

hangman()