import random

# Step 1: Create a list of words
words = ["code", "python", "java", "mango", "linux", "windows", "mac", "software", "pineapple", "hardware"]
secret_word = random.choice(words)  # Pick a random word from the list

# Step 2: Create a variable for dashes
dashes = "-" * len(secret_word)

# Step 3: Function to display the game intro
def display_intro():
    print("************************************")
    print("*       WELCOME TO GUESS THE WORD       *")
    print("* Try to guess the secret word!         *")
    print("* You have 10 incorrect guesses max.    *")
    print("* Only lowercase letters are allowed.   *")
    print("************************************\n")

# Step 4: Function to get a valid guess from the user
def get_guess():
    while True:
        guess = input("Guess: ").strip()
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess

# Step 5: Function to update dashes
def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result

# Step 6: Start the game
display_intro()
guesses_left = 10
guessed_letters = set()

# First guess (without printing dashes initially)
guess = get_guess()

# Game loop
while dashes != secret_word and guesses_left > 0:
    if guess in guessed_letters:
        print("You've already guessed that letter!")
    else:
        guessed_letters.add(guess)
        if guess in secret_word:
            print("That letter is in the word!")
            dashes = update_dashes(secret_word, dashes, guess)
        else:
            print("That letter is not in the word.")
            guesses_left -= 1

    # Print updated word and remaining guesses
    print(dashes)
    print(f"{guesses_left} incorrect guesses left.\n")

    # Get the next guess if game is still running
    if dashes != secret_word and guesses_left > 0:
        guess = get_guess()

# Step 7: Determine the outcome
if dashes == secret_word:
    print(f"🎉 Congrats! You win. The word was: {secret_word}")
else:
    print(f"😞 You lose. The word was: {secret_word}")
