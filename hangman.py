import random

MAX_LIVES = 6
WORDS = {
    "python": "Programming language",
    "github": "Version control platform",
    "coding": "Software development process",
    "binary": "Computer number system",
    "server": "Handles network requests",
}


def select_word():
    """Pick a random word and return it with its hint."""
    return random.choice(list(WORDS.items()))


def render_board(display, lives, guessed_letters):
    """Print the current game board and game status."""
    print("\n" + "=" * 40)
    print("Word:", " ".join(display))
    print("Lives remaining:", lives)
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")
    print("=" * 40)


def get_guess(guessed_letters):
    """Ask the player for a guess and validate the input."""
    guess = input("Guess a letter or the full word: ").strip().lower()

    if not guess:
        print("⚠️ Please enter a letter or word.")
        return None

    if len(guess) == 1 and not guess.isalpha():
        print("⚠️ Please enter a valid letter.")
        return None

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        return None

    return guess


def reveal_letters(word, guess, display):
    """Reveal all matching letters in the display list."""
    correct = False

    for index in range(len(word)):
        if word[index] == guess:
            display[index] = guess
            correct = True

    return correct


def play_game():
    """Main game loop for Hangman."""
    chosen_word, hint = select_word()
    display = ["_"] * len(chosen_word)
    guessed_letters = set()
    lives = MAX_LIVES

    print("🎮 Welcome to ODEAlpha Internship Hangman")
    print("Category: Technology")
    print("Hint:", hint)

    while lives > 0 and "_" in display:
        render_board(display, lives, guessed_letters)

        guess = get_guess(guessed_letters)
        if guess is None:
            continue

        if len(guess) > 1:
            if guess == chosen_word:
                display = list(chosen_word)
                break
            lives -= 2
            print("❌ Wrong word guess! 2 lives deducted.")
            continue

        guessed_letters.add(guess)

        if reveal_letters(chosen_word, guess, display):
            print("✅ Correct guess!")
        else:
            lives -= 1
            print("❌ Wrong guess!")

    if "_" not in display:
        print("\n🎉 Congratulations! You won!")
        print("The word was:", chosen_word)
    else:
        print("\n💀 Game Over")
        print("The word was:", chosen_word)


def main():
    play_game()


if __name__ == "__main__":
    main()
