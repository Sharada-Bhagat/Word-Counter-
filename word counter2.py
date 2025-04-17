# # Word Counter Program

# def count_words(text):
#     """
#     This function takes a string input and returns the number of words in it.
#     Words are considered as sequences separated by spaces.
#     """
#     words = text.strip().split()  # Remove leading/trailing spaces and split by space
#     return len(words)

# def main():
#     print("=== Word Counter ===")
#     print("Enter a sentence or paragraph to count the number of words.")
    
#     # Take user input
#     user_input = input("Your input: ")

#     # Error handling for empty input
#     if not user_input.strip():
#         print("Error: You entered an empty input. Please try again.")
#         return

#     # Count the words using the function
#     word_count = count_words(user_input)

#     # Display the result
#     print(f"\nWord Count: {word_count} word(s)")

# # Run the program
# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import messagebox

def count_words():
    """
    Get text from the text box, count the number of words,
    and display the result in a styled label box.
    """
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("⚠️ Warning", "Please enter some text.")
        return

    words = text.split()
    word_count = len(words)
    word_label = "word" if word_count == 1 else "words"
    result_text = f"🔢 {word_count} {word_label}"

    # Update the result box with styled text
    result_box.config(text=result_text, bg="#dfe6e9", fg="#2d3436")

# Create main window
root = tk.Tk()
root.title("🔠 Word Counter")
root.geometry("600x500")
root.config(bg="#e0f7fa")  # New background

# Title Label with updated color
title = tk.Label(root, text="🔠 Word Counter", font=("Helvetica", 24, "bold"), bg="#e0f7fa", fg="#2e3d49")
title.pack(pady=20)

# Instruction Label
instruction = tk.Label(root, text="Type or paste your paragraph below:", font=("Helvetica", 12), bg="#e0f7fa", fg="#2e3d49")
instruction.pack()

# Styled Text Box
text_input = tk.Text(root, height=10, width=60, font=("Helvetica", 12), wrap="word",
                     bd=2, relief="groove", padx=10, pady=10, bg="#ffffff", fg="#2e3d49")
text_input.pack(pady=15)

# Stylish Count Button with new color
count_button = tk.Button(
    root,
    text="🚀 Count Words",
    command=count_words,
    font=("Helvetica", 14, "bold"),
    bg="#6c5ce7",
    fg="white",
    padx=20,
    pady=8,
    relief="raised",
    bd=3
)
count_button.pack(pady=10)

# Result Box with clean color
result_box = tk.Label(
    root,
    text="",
    font=("Helvetica", 16, "bold"),
    bg="#e0f7fa",  # Default color
    fg="#2e3d49",
    padx=20,
    pady=10,
    bd=2,
    relief="ridge"
)
result_box.pack(pady=20)

# Run the GUI
root.mainloop()


