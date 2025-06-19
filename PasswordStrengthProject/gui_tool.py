import tkinter as tk
from tkinter import messagebox, filedialog
from zxcvbn import zxcvbn
import itertools

# --- Wordlist Generation ---
def generate_wordlist(words):
    suffixes = ['123', '@123', '2024', '2025', '!']
    variants = set()

    for word in words:
        variants.add(word.lower())
        variants.add(word.upper())
        variants.add(word.capitalize())
        for s in suffixes:
            variants.add(word + s)
            variants.add(word.capitalize() + s)

    for combo in itertools.permutations(words, 2):
        variants.add(''.join(combo))

    return list(variants)

# --- GUI Functionality ---
def check_password_strength():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    result = zxcvbn(password)
    score = result['score']
    suggestions = result['feedback']['suggestions']
    suggestion_text = "\n".join(suggestions) if suggestions else "Looks good!"
    result_label.config(text=f"Score: {score}/4\nSuggestions:\n{suggestion_text}")

def create_wordlist():
    inputs = wordlist_entry.get().strip()
    if not inputs:
        messagebox.showwarning("Input Error", "Please enter keywords.")
        return
    words = inputs.split()
    wordlist = generate_wordlist(words)
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Wordlist As",
                                             filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "w") as f:
            for word in wordlist:
                f.write(word + "\n")
        messagebox.showinfo("Success", f"Wordlist saved with {len(wordlist)} entries.")

# --- GUI Layout ---
root = tk.Tk()
root.title("Password Strength & Wordlist Generator")
root.geometry("450x400")
root.resizable(False, False)

tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=5)

result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

tk.Label(root, text="🧠 Wordlist Generator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter words (e.g. name year pet):").pack()
wordlist_entry = tk.Entry(root, width=40)
wordlist_entry.pack(pady=5)

tk.Button(root, text="Generate & Save Wordlist", command=create_wordlist).pack(pady=10)

root.mainloop()
