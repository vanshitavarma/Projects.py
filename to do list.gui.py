import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("500x500")
root.configure(bg="#f4f4f4")

# Task list: [("Task name", is_completed)]
user_list = []

# For filtering tasks
filter_var = tk.StringVar(value="All")
check_vars = []

# Functions
def add_task():
    task = simpledialog.askstring("Add Task", "Enter your new task:")
    if task:
        user_list.append([task, False])
        update_list()

def delete_task():
    indices_to_delete = []
    for i, var in enumerate(check_vars):
        if var.get():
            indices_to_delete.append(i)
    if not indices_to_delete:
        messagebox.showwarning("No Selection", "Select checkbox(es) to delete task(s).")
        return
    for i in reversed(indices_to_delete):
        del user_list[i]
    update_list()

def toggle_status(index):
    user_list[index][1] = not user_list[index][1]
    update_list()

def update_list():
    for widget in list_frame.winfo_children():
        widget.destroy()

    check_vars.clear()
    selected_filter = filter_var.get()

    for i, (task, completed) in enumerate(user_list):
        if selected_filter == "Completed" and not completed:
            continue
        if selected_filter == "Pending" and completed:
            continue

        var = tk.BooleanVar(value=completed)
        cb = tk.Checkbutton(
            list_frame,
            text=task,
            variable=var,
            font=("Arial", 12),
            anchor="w",
            bg="#ffffff",
            command=lambda idx=i: toggle_status(idx)
        )
        cb.pack(fill="x", pady=2, padx=10, anchor="w")
        check_vars.append(var)

def set_filter():
    update_list()

def exit_app():
    root.destroy()

# GUI Elements
title_label = tk.Label(root, text="📋 Your TO-DO LIST", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Filter Radio Buttons
filter_frame = tk.Frame(root, bg="#f4f4f4")
filter_frame.pack(pady=5)

tk.Label(filter_frame, text="View: ", font=("Arial", 10), bg="#f4f4f4").pack(side="left")
tk.Radiobutton(filter_frame, text="All", variable=filter_var, value="All", command=set_filter, bg="#f4f4f4").pack(side="left")
tk.Radiobutton(filter_frame, text="Completed", variable=filter_var, value="Completed", command=set_filter, bg="#f4f4f4").pack(side="left")
tk.Radiobutton(filter_frame, text="Pending", variable=filter_var, value="Pending", command=set_filter, bg="#f4f4f4").pack(side="left")

# Task display area
list_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="sunken")
list_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Button Frame
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="➕ Add Task", command=add_task, width=12, bg="#d1e7dd")
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(btn_frame, text="🗑 Delete Selected", command=delete_task, width=15, bg="#f8d7da")
del_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(btn_frame, text="🚪 Exit", command=exit_app, width=10, bg="#f0ad4e")
exit_btn.grid(row=0, column=2, padx=5)

# Start the app
update_list()
root.mainloop()
