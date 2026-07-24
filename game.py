import random


def play_word_guessing_game():
    # List of hidden words to choose from
    words = [
        "python",
        "developer",
        "algorithm",
        "keyboard",
        "variable",
        "function",
        "terminal",
    ]

    # Game setup
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    max_lives = 3
    lives = max_lives

    print("=" * 40)
    print(" Welcome to the Word Guessing Game!")
    print("=" * 40)
    print(f"Guess the word before running out of lives! You have {max_lives} lives.\n")

    while lives > 0:
        # Display the current state of the word (e.g., "p _ t h o n")
        display_word = [
            letter if letter in guessed_letters else "_" for letter in secret_word
        ]
        print("Word: " + " ".join(display_word))

        # Check for win condition
        if "_" not in display_word:
            print(
                "\n Congratulations! You guessed the word correctly:",
                secret_word,
            )
            break

        # Display current status
        print(f"Lives remaining: {lives}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Get user input
        guess = input("Guess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(f" You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Process the guess
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f" Good job! '{guess}' is in the word.\n")
        else:
            lives -= 1
            print(f" Sorry, '{guess}' is not in the word.\n")

    # Loss condition
    if lives == 0:
        print("=" * 40)
        print(f" Game Over! You ran out of lives. The word was: '{secret_word}'")
        print("=" * 40)


if __name__ == "__main__":
    play_word_guessing_game()
