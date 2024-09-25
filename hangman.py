import random

# List of words for the game
word_list = ["python", "hangman", "developer", "coding", "programming", "algorithm", "function", "variable", "debugging"]

# Function to display the Hangman stages based on attempts left
def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,  # final state: head, torso, both arms, both legs
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,  # head, torso, both arms, one leg
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,  # head, torso, both arms
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,  # head, torso, one arm
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,  # head and torso
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,  # head
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """   # initial empty state
    ]
    return stages[attempts]

# Function to choose a word from the list
def get_word():
    return random.choice(word_list)

# Function to play the Hangman game
def play_game():
    word = get_word()
    word_completion = "_" * len(word)  # Word representation to be displayed (e.g., _ _ _ _ _)
    guessed = False
    guessed_letters = []  # List of guessed letters
    guessed_words = []    # List of guessed words
    attempts = 6  # Number of attempts allowed

    print("Let's play Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")

    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").lower()

        # Validate input
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                # Reveal guessed letters in word_completion
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != word:
                print(f"{guess} is not the correct word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please guess a letter or the entire word.")

        print(display_hangman(attempts))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word}'. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_game()