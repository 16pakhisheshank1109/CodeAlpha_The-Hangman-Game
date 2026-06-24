import random

# Technology-themed words and hints
words = {
    "python": "Programming Language",
    "github": "Version Control Platform",
    "coding": "Creating Software",
    "binary": "Computer Number System",
    "server": "Handles Network Requests"
}

# Select random word
chosen_word = random.choice(list(words.keys()))
hint = words[chosen_word]

# Create blanks
display = ["_"] * len(chosen_word)

# Track guessed letters
guessed_letters = set()

# Number of lives
lives = 6

print("🎮 Welcome to Hangman Game!")
print("Category: Technology")
print("Hint:", hint)

# Main game loop
while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Lives Left:", lives)

    guess = input("Guess a letter or the full word: ").lower()

    # Validate input
    if not guess:
        print("⚠️ Please enter a letter or word!")
        continue

    # Full word guess
    if len(guess) > 1:

        if guess == chosen_word:
            display = list(chosen_word)
            print("\n🎉 Amazing! You guessed the whole word!")
            break

        else:
            lives -= 2
            print("❌ Wrong word guess! 2 lives deducted.")

    # Single letter guess
    else:

        if not guess.isalpha():
            print("⚠️ Please enter a valid letter!")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:

            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess

            print("✅ Correct Guess!")

        else:
            lives -= 1
            print("❌ Wrong Guess!")

# Final result
if "_" not in display:
    print("\n🎉 Congratulations! You Won!")
    print("The word was:", chosen_word)

else:
    print("\n💀 Game Over!")
    print("The word was:", chosen_word)