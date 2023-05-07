import tkinter as tk
import random
import time

# Define a list of words
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Define the timer for the typing test
def start_timer():
    global start_time
    start_time = time.time()

# Calculate the typing speed
def calculate_speed():
    total_time = time.time() - start_time
    speed = len(user_input.get()) / total_time * 60
    speed_label.config(text=f"Your typing speed is: {speed:.2f} words per minute")

# Display the next word for typing
def next_word():
    word = random.choice(words)
    word_label.config(text=word)
    user_input.delete(0, tk.END)

# Check if the typed word matches the displayed word
def check_word(event):
    if user_input.get() == word_label.cget("text"):
        next_word()
        calculate_speed()

# Create the main window
window = tk.Tk()
window.title("Typing Test")

# Create the labels for the word to type and the typing speed
word_label = tk.Label(window, font=("Arial", 24))
word_label.pack()
next_word()

speed_label = tk.Label(window, font=("Arial", 18))
speed_label.pack()

# Create the entry widget for the user input
user_input = tk.Entry(window, font=("Arial", 24))
user_input.pack()
user_input.bind("<Return>", check_word)

# Create the start button and the timer label
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack()

timer_label = tk.Label(window, font=("Arial", 18))
timer_label.pack()

# Update the timer label every second
def update_timer():
    if "start_time" in globals():
        elapsed_time = time.time() - start_time
        timer_label.config(text=f"Time elapsed: {elapsed_time:.0f} seconds")
    window.after(1000, update_timer)

update_timer()

# Run the window
window.mainloop()
