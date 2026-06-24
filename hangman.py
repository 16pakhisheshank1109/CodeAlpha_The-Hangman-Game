import random
from typing import Dict, List, Set, Tuple

MAX_LIVES = 6
WORDS: Dict[str, str] = {
    "python": "Programming language",
    "github": "Version control platform",
    "coding": "Software development process",
    "binary": "Computer number system",
    "server": "Handles network requests",
}


def select_word() -> Tuple[str, str]:
    """Choose a random word and return it with a hint."""
    return random.choice(list(WORDS.items()))


def render_board(display: List[str], lives: int, guessed_letters: Set[str]) -> None:
    """Print the current game board and status."""
    print("\n" + "=" * 60)
    print("Word:", " ".join(display))
    print(f"Lives remaining: {lives}")
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")
    print("=" * 60)


def get_guess(guessed_letters: Set[str]) -> str:
    """Read and validate a guess from the player."""
    guess = input("Guess a letter or the full word: ").strip().lower()

    if not guess:
        raise ValueError("Please enter a letter or word.")

    if len(guess) == 1 and not guess.isalpha():
        raise ValueError("Please enter a valid letter.")

    if guess in guessed_letters:
        raise ValueError("You already guessed that letter.")

    return guess


def reveal_letters(word: str, guess: str, display: List[str]) -> bool:
    """Reveal guessed letters in the display and return if the guess was correct."""
    correct = False
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = letter
            correct = True
    return correct


def play_game() -> None:
    """Run the Hangman game loop."""
    chosen_word, hint = select_word()
    display = ["_"] * len(chosen_word)
    guessed_letters: Set[str] = set()
    lives = MAX_LIVES

    print("🎮 Welcome to CodeAlpha Hangman")
    print("Category: Technology")
    print("Hint:", hint)

    while lives > 0 and "_" in display:
        render_board(display, lives, guessed_letters)

        try:
            guess = get_guess(guessed_letters)
        except ValueError as error:
            print("⚠️", error)
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
        print("\n🎉 Congratulations — you won!")
        print("The word was:", chosen_word)
    else:
        print("\n💀 Game Over")
        print("The word was:", chosen_word)


def main() -> None:
    """Entry point for the Hangman application."""
    play_game()


if __name__ == "__main__":
    main()
