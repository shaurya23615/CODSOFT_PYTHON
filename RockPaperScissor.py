import tkinter as tk
import random

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("🎮 Rock Paper Scissors")

root.geometry("620x760")
root.minsize(620, 760)

root.config(bg="#0f172a")
root.resizable(True, True)

# ---------------- VARIABLES ---------------- #
user_score = 0
computer_score = 0
round_number = 1

choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# ---------------- TITLE ---------------- #
title = tk.Label(
    root,
    text="🔥 Rock Paper Scissors 🔥",
    font=("Comic Sans MS", 28, "bold"),
    bg="#0f172a",
    fg="#facc15"
)
title.pack(pady=12)

# ---------------- SUBTITLE ---------------- #
subtitle = tk.Label(
    root,
    text="Choose your move and defeat the computer!",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
subtitle.pack(pady=5)

# ---------------- PLAYER CHOICE ---------------- #
user_choice_label = tk.Label(
    root,
    text="👦 Your Choice:",
    font=("Arial", 18, "bold"),
    bg="#1e293b",
    fg="#22c55e",
    width=30,
    pady=10
)
user_choice_label.pack(pady=10)

# ---------------- COMPUTER CHOICE ---------------- #
computer_choice_label = tk.Label(
    root,
    text="💻 Computer Choice:",
    font=("Arial", 18, "bold"),
    bg="#1e293b",
    fg="#fb7185",
    width=30,
    pady=10
)
computer_choice_label.pack(pady=10)

# ---------------- RESULT LABEL ---------------- #
result_label = tk.Label(
    root,
    text="✨ Result Will Appear Here ✨",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="white"
)
result_label.pack(pady=18)

# ---------------- SCORE BOARD ---------------- #
score_label = tk.Label(
    root,
    text="👦 You: 0    🤖 Computer: 0",
    font=("Arial", 18, "bold"),
    bg="#7c3aed",
    fg="white",
    padx=20,
    pady=10
)
score_label.pack(pady=10)

# ---------------- ROUND LABEL ---------------- #
round_label = tk.Label(
    root,
    text="🎯 Round: 1",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="#f97316"
)
round_label.pack(pady=10)

# ---------------- GAME FUNCTION ---------------- #
def play(user_choice):
    global user_score, computer_score, round_number

    computer_choice = random.choice(list(choices.keys()))

    # Show choices
    user_choice_label.config(
        text=f"👦 Your Choice: {choices[user_choice]} {user_choice}"
    )

    computer_choice_label.config(
        text=f"💻 Computer Choice: {choices[computer_choice]} {computer_choice}"
    )

    # Winner Logic
    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        result_color = "#facc15"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        result_color = "#22c55e"
        user_score += 1

    else:
        result = "😢 Computer Wins!"
        result_color = "#ef4444"
        computer_score += 1

    # Show Result
    result_label.config(
        text=result,
        fg=result_color
    )

    # Increase Round
    round_number += 1

    # After 5 Rounds
    if round_number > 5:

        if user_score > computer_score:
            result_label.config(
                text="🏆 You Won The Match!",
                fg="#22c55e"
            )

        elif computer_score > user_score:
            result_label.config(
                text="💻 Computer Won The Match!",
                fg="#ef4444"
            )

        else:
            result_label.config(
                text="🤝 Match Draw!",
                fg="#facc15"
            )

        # Reset Everything
        user_score = 0
        computer_score = 0
        round_number = 1

    # Update Score
    score_label.config(
        text=f"👦 You: {user_score}    🤖 Computer: {computer_score}"
    )

    # Update Round
    round_label.config(
        text=f"🎯 Round: {round_number}"
    )

# ---------------- BUTTON FRAME ---------------- #
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=25)

# ---------------- ROCK BUTTON ---------------- #
rock_btn = tk.Button(
    button_frame,
    text="🪨 ROCK",
    font=("Arial", 16, "bold"),
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    width=11,
    height=1,
    bd=0,
    cursor="hand2",
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

# ---------------- PAPER BUTTON ---------------- #
paper_btn = tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 16, "bold"),
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    width=11,
    height=1,
    bd=0,
    cursor="hand2",
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

# ---------------- SCISSORS BUTTON ---------------- #
scissors_btn = tk.Button(
    button_frame,
    text="✂️ SCISSORS",
    font=("Arial", 14, "bold"),
    bg="#10b981",
    fg="white",
    activebackground="#059669",
    width=13,
    height=1,
    bd=0,
    cursor="hand2",
    padx=2,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

# ---------------- RESET FUNCTION ---------------- #
def reset_game():
    global user_score, computer_score, round_number

    user_score = 0
    computer_score = 0
    round_number = 1

    user_choice_label.config(
        text="👦 Your Choice:"
    )

    computer_choice_label.config(
        text="💻 Computer Choice:"
    )

    result_label.config(
        text="✨ Result Will Appear Here ✨",
        fg="white"
    )

    score_label.config(
        text="👦 You: 0    🤖 Computer: 0"
    )

    round_label.config(
        text="🎯 Round: 1"
    )

# ---------------- RESET BUTTON ---------------- #
reset_btn = tk.Button(
    root,
    text="🔄 Reset Game",
    font=("Arial", 16, "bold"),
    bg="#f97316",
    fg="white",
    activebackground="#ea580c",
    width=18,
    height=1,
    bd=0,
    cursor="hand2",
    command=reset_game
)
reset_btn.pack(pady=15)

# ---------------- EXIT BUTTON ---------------- #
exit_btn = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 16, "bold"),
    bg="#e11d48",
    fg="white",
    activebackground="#be123c",
    width=18,
    height=1,
    bd=0,
    cursor="hand2",
    command=root.quit
)
exit_btn.pack(pady=10)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Made with ❤️ using Python Tkinter",
    font=("Arial", 11, "italic"),
    bg="#0f172a",
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=15)

# ---------------- RUN APP ---------------- #
root.mainloop()