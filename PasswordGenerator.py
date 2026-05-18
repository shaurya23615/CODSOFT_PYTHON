import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("🔐 Password Generator")

root.geometry("760x620")
root.minsize(760, 620)

bg_color = "#0F172A"
card_color = "#111827"

primary = "#6366F1"
success = "#10B981"
danger = "#EF4444"

text_color = "#E2E8F0"
muted_text = "#94A3B8"

root.config(bg=bg_color)

title = tk.Label(
    root,
    text=" Strong Password Generator ",
    font=("Arial", 28, "bold"),
    bg=bg_color,
    fg=text_color
)
title.pack(pady=(30, 10))

subtitle = tk.Label(
    root,
    text="Generate secure and random passwords instantly 🛡️",
    font=("Arial", 15),
    bg=bg_color,
    fg=muted_text
)
subtitle.pack(pady=5)

length_frame = tk.Frame(
    root,
    bg=bg_color
)
length_frame.pack(pady=25)

length_label = tk.Label(
    length_frame,
    text="🔢 Password Length:",
    font=("Arial", 16, "bold"),
    bg=bg_color,
    fg=primary
)
length_label.grid(row=0, column=0, padx=15)

length_spinbox = tk.Spinbox(
    length_frame,
    from_=4,
    to=50,
    font=("Arial", 15),
    width=6,
    justify="center",
    bg=card_color,
    fg=text_color,
    bd=2,
    relief="solid",
    buttonbackground=primary,
    insertbackground=text_color
)
length_spinbox.grid(row=0, column=1)

password_frame = tk.Frame(
    root,
    bg=card_color,
    bd=2,
    relief="solid"
)
password_frame.pack(pady=20, ipadx=40, ipady=4)

password_title = tk.Label(
    password_frame,
    text="🔒 Generated Password",
    font=("Arial", 18, "bold"),
    bg=card_color,
    fg=text_color
)
password_title.pack(pady=(2, 4))

password_label = tk.Label(
    password_frame,
    text="",
    font=("Consolas", 16, "bold"),
    bg=card_color,
    fg=success
)
password_label.pack(pady=4)

def generate_password():

    length = int(length_spinbox.get())

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    password_label.config(
        text=password
    )

def copy_password():

    password = password_label.cget("text")

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )

button_frame = tk.Frame(
    root,
    bg=bg_color
)
button_frame.pack(pady=25)

generate_btn = tk.Button(
    button_frame,
    text="⚡ Generate Password",
    font=("Arial", 16, "bold"),
    bg=primary,
    fg="white",
    activebackground="#4F46E5",
    activeforeground="white",
    width=18,
    height=1,
    bd=0,
    cursor="hand2",
    command=generate_password
)
generate_btn.grid(row=0, column=0, padx=12)

copy_btn = tk.Button(
    button_frame,
    text="📋 Copy Password",
    font=("Arial", 16, "bold"),
    bg=card_color,
    fg=text_color,
    activebackground="#1E293B",
    activeforeground="white",
    width=18,
    height=1,
    bd=0,
    cursor="hand2",
    command=copy_password
)
copy_btn.grid(row=0, column=1, padx=12)

def reset_all():

    password_label.config(
        text=""
    )

    length_spinbox.delete(0, "end")
    length_spinbox.insert(0, "4")

reset_btn = tk.Button(
    root,
    text="🔄 Reset",
    font=("Arial", 16, "bold"),
    bg=bg_color,
    fg=danger,
    activebackground=bg_color,
    activeforeground=danger,
    width=28,
    height=1,
    bd=2,
    relief="solid",
    cursor="hand2",
    command=reset_all
)
reset_btn.pack(pady=20)

exit_btn = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 15, "bold"),
    bg=danger,
    fg="white",
    activebackground="#DC2626",
    activeforeground="white",
    width=14,
    height=1,
    bd=0,
    cursor="hand2",
    command=root.quit
)
exit_btn.pack(pady=10)

length_spinbox.delete(0, "end")
length_spinbox.insert(0, "4")

root.mainloop()