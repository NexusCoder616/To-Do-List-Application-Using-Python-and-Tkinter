# To-Do List Application Using Python and Tkinter

A simple and user-friendly **To-Do List Application** built using **Python** and **Tkinter**.  
This application helps users manage daily tasks with features like adding, updating, completing, removing, and saving tasks.

---

## Features

- Add new tasks
- Mark tasks as completed
- Update existing tasks
- Remove tasks
- Save tasks permanently using a text file
- Simple graphical user interface (GUI)
- Task persistence using file handling

---

## Technologies Used

- **Python 3**
- **Tkinter** (GUI Library)
- **File Handling**

---

## Project Structure

```bash
├── index.py       # Main application file
├── tasks.txt      # Stores saved tasks
└── README.md      # Project documentation
```

---

## How It Works

- Tasks are stored in a list using a custom `Task` class.
- Each task contains:
  - Task title
  - Completion status
- Tasks are automatically loaded from `tasks.txt` when the application starts.
- Users can save tasks before exiting the application.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/todo-list-python.git
```

### 2. Navigate to Project Folder

```bash
cd todo-list-python
```

### 3. Run the Application

```bash
python index.py
```

---

## Requirements

Make sure Python is installed on your system.

Check version:

```bash
python --version
```

Tkinter usually comes pre-installed with Python.

---

## GUI Preview

The application window contains:

- Task display area
- Input field
- Add Task button
- Mark Completed button
- Update Task button
- Remove Task button
- Save & Exit button

---

## Sample Task Format

Tasks are saved in `tasks.txt` like this:

```txt
do groceries|False
Finish project|True
```

- `True` → Completed
- `False` → Pending

---

## Learning Concepts Used

This project demonstrates:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Tkinter GUI development
- File handling in Python
- Event-driven programming

---

## Future Improvements

- Add task deadlines
- Add dark mode
- Add task categories
- Add search functionality
- Add priority levels

---

## Author

Created by **Jathin Kothuri**

---

## License

This project is open-source and available under the MIT License.
