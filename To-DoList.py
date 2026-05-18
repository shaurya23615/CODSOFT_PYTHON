import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("🌟 Daily Planner")
root.geometry("900x650")
root.config(bg="#111827")

# ---------------- COLORS ---------------- #
bg_color = "#111827"
card_color = "#1F2937"

orange = "#F97316"
yellow = "#FACC15"
pink = "#EC4899"
purple = "#8B5CF6"
green = "#10B981"
blue = "#3B82F6"

text_dark = "#F8FAFC"
text_light = "#CBD5E1"

# ---------------- TITLE ---------------- #
title = tk.Label(
    root,
    text="🌈 My Daily To-Do Planner",
    font=("Comic Sans MS", 30, "bold"),
    bg=bg_color,
    fg=orange
)
title.pack(pady=(20, 5))

# ---------------- SUBTITLE ---------------- #
subtitle = tk.Label(
    root,
    text="Plan your day beautifully ✨",
    font=("Arial", 15, "italic"),
    bg=bg_color,
    fg=text_light
)
subtitle.pack()

# ---------------- MAIN CARD ---------------- #
main_card = tk.Frame(
    root,
    bg=card_color,
    bd=0
)
main_card.pack(
    pady=25,
    padx=40,
    fill="both",
    expand=True
)

# ---------------- INPUT SECTION ---------------- #
input_frame = tk.Frame(
    main_card,
    bg=card_color
)
input_frame.pack(pady=20)

task_entry = tk.Entry(
    input_frame,
    font=("Arial", 18),
    width=35,
    bg="#374151",
    fg=text_dark,
    insertbackground=text_dark,
    relief="flat",
    bd=8
)
task_entry.grid(row=0, column=0, padx=10)

# ---------------- FUNCTIONS ---------------- #
def add_task():

    task = task_entry.get()

    if task == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a task!"
        )
        return

    task_listbox.insert(tk.END, "🌟 " + task)

    task_entry.delete(0, tk.END)

# ---------------- UPDATE FUNCTION ---------------- #
def update_task():

    try:
        selected = task_listbox.curselection()[0]

        updated_task = task_entry.get()

        if updated_task == "":
            messagebox.showwarning(
                "Warning",
                "Enter updated task!"
            )
            return

        task_listbox.delete(selected)

        task_listbox.insert(
            selected,
            "✏️ " + updated_task
        )

        task_entry.delete(0, tk.END)

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task to update!"
        )

# ---------------- DELETE FUNCTION ---------------- #
def delete_task():

    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task first!"
        )

# ---------------- COMPLETE FUNCTION ---------------- #
def complete_task():

    try:
        selected = task_listbox.curselection()[0]

        task = task_listbox.get(selected)

        task_listbox.delete(selected)

        task_listbox.insert(
            selected,
            "✅ " + task
        )

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task!"
        )

# ---------------- CLEAR FUNCTION ---------------- #
def clear_tasks():

    task_listbox.delete(0, tk.END)

# ---------------- BUTTON SECTION ---------------- #
button_frame = tk.Frame(
    main_card,
    bg=card_color
)
button_frame.pack(pady=10)

# ---------------- ADD BUTTON ---------------- #
add_btn = tk.Button(
    button_frame,
    text="➕ Add Task",
    font=("Arial", 13, "bold"),
    bg=orange,
    fg="white",
    activebackground="#EA580C",
    activeforeground="white",
    width=14,
    relief="flat",
    cursor="hand2",
    command=add_task
)
add_btn.grid(row=0, column=0, padx=8)

# ---------------- UPDATE BUTTON ---------------- #
update_btn = tk.Button(
    button_frame,
    text="✏️ Update",
    font=("Arial", 13, "bold"),
    bg=blue,
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    width=14,
    relief="flat",
    cursor="hand2",
    command=update_task
)
update_btn.grid(row=0, column=1, padx=8)

# ---------------- COMPLETE BUTTON ---------------- #
complete_btn = tk.Button(
    button_frame,
    text="✅ Complete",
    font=("Arial", 13, "bold"),
    bg=green,
    fg="white",
    activebackground="#0F766E",
    activeforeground="white",
    width=14,
    relief="flat",
    cursor="hand2",
    command=complete_task
)
complete_btn.grid(row=0, column=2, padx=8)

# ---------------- DELETE BUTTON ---------------- #
delete_btn = tk.Button(
    button_frame,
    text="🗑 Delete",
    font=("Arial", 13, "bold"),
    bg=pink,
    fg="white",
    activebackground="#BE185D",
    activeforeground="white",
    width=14,
    relief="flat",
    cursor="hand2",
    command=delete_task
)
delete_btn.grid(row=0, column=3, padx=8)

# ---------------- TASK FRAME ---------------- #
task_frame = tk.Frame(
    main_card,
    bg="#111827",
    bd=3,
    relief="ridge"
)
task_frame.pack(pady=25)

# ---------------- SCROLLBAR ---------------- #
scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ---------------- TASK LISTBOX ---------------- #
task_listbox = tk.Listbox(
    task_frame,
    width=55,
    height=14,
    font=("Arial", 16),
    bg="#1E293B",
    fg="#F8FAFC",
    selectbackground=purple,
    selectforeground="white",
    bd=0,
    yscrollcommand=scrollbar.set
)
task_listbox.pack(padx=10, pady=10)

scrollbar.config(command=task_listbox.yview)

# ---------------- BOTTOM BUTTONS ---------------- #
bottom_frame = tk.Frame(
    main_card,
    bg=card_color
)
bottom_frame.pack(pady=10)

# ---------------- CLEAR BUTTON ---------------- #
clear_btn = tk.Button(
    bottom_frame,
    text="🧹 Clear All",
    font=("Arial", 14, "bold"),
    bg=yellow,
    fg="#111827",
    activebackground="#EAB308",
    activeforeground="#111827",
    width=16,
    relief="flat",
    cursor="hand2",
    command=clear_tasks
)
clear_btn.grid(row=0, column=0, padx=12)

# ---------------- EXIT BUTTON ---------------- #
exit_btn = tk.Button(
    bottom_frame,
    text="❌ Exit",
    font=("Arial", 14, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#1E293B",
    activeforeground="white",
    width=16,
    relief="flat",
    cursor="hand2",
    command=root.quit
)
exit_btn.grid(row=0, column=1, padx=12)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Made with ❤️ using Python Tkinter",
    font=("Arial", 11, "italic"),
    bg=bg_color,
    fg=text_light
)
footer.pack(pady=10)

# ---------------- RUN APP ---------------- #
root.mainloop()