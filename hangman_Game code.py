import random

word_list = [
    "python",
    "java",
    "software",
    "django",
    "mango",
    "pytorch",
    "tensorflow",
]

hangman_stages = [
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    =========
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      /
    |
    =========
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |
    |
    =========
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |
    |
    =========
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    =========
    """,
    """
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    =========
    """,
    """
     _______
    |/      |
    |
    |
    |
    |
    |
    =========
    """,
]

lives = 6
chosen_word = random.choice(word_list)

# Uncomment the next line for debugging if you want to see the chosen word
# print(f"DEBUG: chosen word is {chosen_word}")

display = ["_"] * len(chosen_word)

print("Welcome to Hangman!")
print(" ".join(display))

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower().strip()
    if not guessed_letter or len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("Please enter a single letter.")
        continue

    if guessed_letter in display:
        print(f"You already guessed '{guessed_letter}'.")
    else:
        if guessed_letter in chosen_word:
            for position, letter in enumerate(chosen_word):
                if letter == guessed_letter:
                    display[position] = guessed_letter
        else:
            lives -= 1
            print(f"Wrong guess. Lives remaining: {lives}")
            if lives == 0:
                game_over = True
                print("You lose!!")
                print(f"The word was: {chosen_word}")
                break

    print(" ".join(display))
    print(hangman_stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!!")
