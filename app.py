import tkinter as tk
import random

# Predefined word list
words = ["python", "hangman", "programming", "game", "challenge"]

# Pick a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts_left = 6
guessed_letters = []


def update_display():
    """Update word, attempts, and guessed letters"""
    word_display.config(text=" ".join(guessed))
    attempts_display.config(text=f"Attempts left: {attempts_left}")
    letters_display.config(text=f"Guessed: {', '.join(guessed_letters)}")


def draw_hangman():
    """Draw parts of hangman based on wrong attempts"""
    wrong = 6 - attempts_left

    if wrong == 1:  # base
        canvas.create_line(20, 250, 180, 250, width=3)
    elif wrong == 2:  # pole
        canvas.create_line(50, 250, 50, 50, width=3)
    elif wrong == 3:  # top bar
        canvas.create_line(50, 50, 150, 50, width=3)
        canvas.create_line(150, 50, 150, 80, width=3)
    elif wrong == 4:  # head
        canvas.create_oval(130, 80, 170, 120, width=3)
    elif wrong == 5:  # body
        canvas.create_line(150, 120, 150, 180, width=3)
    elif wrong == 6:  # arms + legs
        canvas.create_line(150, 140, 120, 160, width=3)  # left arm
        canvas.create_line(150, 140, 180, 160, width=3)  # right arm
        canvas.create_line(150, 180, 120, 210, width=3)  # left leg
        canvas.create_line(150, 180, 180, 210, width=3)  # right leg


def guess_letter():
    """Handle guessed letter"""
    global attempts_left

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        result_display.config(text="Enter a single valid letter!")
        return

    if letter in guessed_letters:
        result_display.config(text=f"You already guessed '{letter}'")
        return

    guessed_letters.append(letter)

    if letter in word:
        for i, ch in enumerate(word):
            if ch == letter:
                guessed[i] = letter
        result_display.config(text=f"Good guess! '{letter}' is in the word.")
    else:
        attempts_left -= 1
        result_display.config(text=f"Wrong! '{letter}' not in the word.")
        draw_hangman()

    update_display()
    check_game_over()


def check_game_over():
    """Check win/lose conditions"""
    if "_" not in guessed:
        result_display.config(text="🎉 Congratulations! You won!")
        entry.config(state="disabled")
        guess_button.config(state="disabled")
    elif attempts_left == 0:
        result_display.config(text=f"😢 Game Over! The word was '{word}'")
        entry.config(state="disabled")
        guess_button.config(state="disabled")


# GUI setup
root = tk.Tk()
root.title("Hangman Game")

# Word display
word_display = tk.Label(root, text=" ".join(guessed), font=("Helvetica", 20))
word_display.pack(pady=10)

# Attempts display
attempts_display = tk.Label(root, text=f"Attempts left: {attempts_left}", font=("Helvetica", 14))
attempts_display.pack(pady=5)

# Guessed letters display
letters_display = tk.Label(root, text="Guessed: ", font=("Helvetica", 12))
letters_display.pack(pady=5)

# Canvas for hangman drawing
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=5)

# Guess button
guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 14))
guess_button.pack(pady=5)

# Result display
result_display = tk.Label(root, text="", font=("Helvetica", 12))
result_display.pack(pady=10)

# Initialize
update_display()

root.mainloop()
