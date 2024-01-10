import random
import time
import os

def generate_words_list(file_path):
    words = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 5:
                words.append(line)
    return words


def display():
    global cursor_position
    for i in list_of_guesses:
        for key, value in i:
            if value == 1:
                print(f"\x1b[1;97m{key}\x1b[0m", end=' ')
            elif value == 2:
                print(f"\x1b[1;93m{key}\x1b[0m", end=' ')
            elif value == 3:
                print(f"\x1b[1;95m{key}\x1b[0m", end=' ')
        print()
        cursor_position += 1


def defects(guess):
    global cursor_position
    if len(guess) != 5:
        print("Only 5 letter words buddy, try again")
        cursor_position += 2
        return False
    else:
        for i in range(10):
            if str(i) in guess:
                print("Only english alphabet allowed")
                cursor_position += 2
                return False
        return True


cursor_position = 1
# list_of_words = ['apple', 'books', 'heart', 'birch', 'bitch', 'batch', 'catch', 'hitch']
list_of_words = generate_words_list('words_alpha.txt')
random_choice = random.choice(list_of_words)
guess = ''
guesses = []
list_of_guesses = []
guesses_left = 6
flag_started_guessing = False

'''
Here we are denoting correct, present and not present by numbers

1 -> correct [green]
2 -> present [yellow]
3 -> not present [magenta]
'''
os.system('cls')
print("Hello There!!!")
time.sleep(1)
print("Welcome to Wordle!")
time.sleep(1.2)
print("\x1b[1;97mwhite\x1b[0m: denotes correct letter")
time.sleep(0.4)
print("\x1b[1;93myellow\x1b[0m: denotes letter is present somewhere in the word")
time.sleep(0.3)
print("\x1b[1;95mmagenta\x1b[0m: denotes letter is not present anywhere in the word")
time.sleep(0.7)
print("Let's start guessing!")
while guesses_left != 0:
    guesses = []
    print(f"You have {guesses_left} guesses left")
    cursor_position += 1
    guess = input("\x1b[34m>\x1b[0m")
    if guess == random_choice:
        print("Congratulations, that's the word!!!")
        break
    else:
        # Cataloging the letters of guessed word as correct, present and not present as list of tuples
        for i, j in zip(guess, random_choice):
            if i == j:
                guesses.append((i, 1))
            elif i in random_choice:
                guesses.append((i, 2))
            else:
                guesses.append((i, 3))

        verdict = defects(guess=guess)

        if verdict:
            guesses_left -= 1
            list_of_guesses.append(guesses)
            if len(list_of_guesses) > 1:
                print(f"\x1b[{cursor_position}A", end='')
                print("\x1b[0J", end='')
                cursor_position = 1
            display()
        elif not verdict:
            continue

if guesses_left == 0:
    print("Oooohhhhhhhh, too bad you couldn't guess it")
    time.sleep(0.7)
    print(f"The word was {random_choice}")