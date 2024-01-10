import random

def generate_words_list(file_path):
    words = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 5:
                words.append(line)

    return words

# List of 5-letter words (you can add more words to this list)
word_list = generate_words_list("G:\CS4811_AI_NIRMAL\TEAM_PRJ_WORDLE\words_alpha.txt")

# Select a random word from the list
target_word = random.choice(word_list)

# Initialize the game state
attempts = 6
guessed_letters = set()
correct_word = list('_' * len(target_word))

# Main game loop
while attempts > 0:
    # Display the current state of the word
    print(" ".join(correct_word))

    # Ask the player for a guess
    guess = input(f"Attempt {attempts}: Enter a 5-letter word guess: ").lower()

    # Check if the guess is valid
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue

    # Check if the guess is correct
    if guess == target_word:
        print("Congratulations! You've guessed the word:", target_word)
        break

    # Update the game state based on the guess
    attempts -= 1
    guessed_letters.add(guess)

    # Check for correct letters in correct positions and incorrect positions
    for i in range(len(target_word)):
        if guess[i] == target_word[i]:
            correct_word[i] = '\x1b[32m' + guess[i] + '\x1b[0m'  # Green for correct position
        elif guess[i] in target_word:
            correct_word[i] = '\x1b[33m' + guess[i] + '\x1b[0m'  # Yellow for incorrect position

    # Display guessed letters
    print("Guessed letters:", " ".join(guessed_letters))

# If the player runs out of attempts, reveal the correct word
if attempts == 0:
    print("Sorry, you're out of attempts. The correct word was:", target_word)
