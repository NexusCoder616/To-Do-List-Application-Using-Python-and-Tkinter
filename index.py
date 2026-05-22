import tkinter as tk
from tkinter import messagebox
import os

# Task Class
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_completed(self):
        """Mark task as completed"""
        self.completed = True

    def __str__(self):
        return f"{self.title} - [{'Done' if self.completed else 'Pending'}]"

# File Handling
TASK_FILE = "tasks.txt"

def save_tasks(tasks):
    """Save tasks to a file"""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            # Convert boolean to string explicitly
            completed_str = "True" if task.completed else "False"
            file.write(f"{task.title}|{completed_str}\n")
            print(f"Saving tasks to: {os.path.abspath(TASK_FILE)}")

def load_tasks():
    """Load tasks from a file"""
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                title, completed = line.strip().split("|")
                tasks.append(Task(title, completed == "True"))
    return tasks

# Tkinter GUI
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")

        self.tasks = load_tasks()

        # Title Label
        tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Input Field
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5, pady=2)

        self.complete_button = tk.Button(self.button_frame, text="Mark Completed", command=self.mark_completed, bg="#2196F3", fg="white")
        self.complete_button.grid(row=0, column=1, padx=5, pady=2)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, bg="#FFC107", fg="black")
        self.update_button.grid(row=1, column=0, padx=5, pady=2)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task, bg="#F44336", fg="white")
        self.remove_button.grid(row=1, column=1, padx=5, pady=2)

        self.save_button = tk.Button(root, text="Save & Exit", command=self.save_and_exit, bg="#9E9E9E", fg="white")
        self.save_button.pack(pady=10)

        self.load_tasks_into_listbox()

    def load_tasks_into_listbox(self):
        """Loads tasks into the listbox"""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def add_task(self):
        """Adds a new task"""
        title = self.entry.get().strip()
        if title:
            self.tasks.append(Task(title))
            self.entry.delete(0, tk.END)
            self.load_tasks_into_listbox()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_completed(self):
        """Marks a selected task as completed"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index].mark_completed()
            self.load_tasks_into_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def update_task(self):
        """Updates the selected task"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_title = self.entry.get().strip()
            if new_title:
                self.tasks[selected_index].title = new_title
                self.entry.delete(0, tk.END)
                self.load_tasks_into_listbox()
            else:
                messagebox.showwarning("Warning", "Task title cannot be empty!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def remove_task(self):
        """Removes the selected task"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.load_tasks_into_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def save_and_exit(self):
        """Saves tasks to file and exits the program"""
        save_tasks(self.tasks)
        self.root.destroy()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
