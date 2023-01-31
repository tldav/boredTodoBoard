import tkinter as tk
import customtkinter as ctk
import requests as api
import json
from tkinter import ttk


# API
API_URL = "http://localhost:8000/todo"


def fetchTodos():
    try:
        res = api.get(API_URL)
        todos = json.loads(res.text)
        return todos
    except Exception as e:
        print(e)


def postTodo(todo):
    reqBody = {
        "title": todo["title"],
        "body": todo["body"]
    }
    try:
        res = api.post(url=API_URL, json=reqBody)
        return json.loads(res.text)
    except Exception as e:
        print(e)


def deleteTodo(id):
    url = "{}/{}".format(API_URL, id)
    try:
        res = api.delete(url)
    except Exception as e:
        print(e)


# TKInter initialization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.winfo_toplevel().title("Bored Todo Board")
root.geometry("800x800")

# Style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="#3b3b3b",
                foreground="white", fieldbackground="#3b3b3b")
style.configure("Treeview.Heading", background="#2b2b2b",
                foreground="white", font=("Roboto", 10))
style.layout("Treeview", [
    ('Treeview.treearea', {'sticky': 'nswe'})
])

# Todos Display region
todoTable = ttk.Treeview(root)
todoTable["show"] = "headings"  # hides default first column
todoTable['columns'] = ("Task", "Description")

todoTable.column("Task", anchor=tk.W, width=75, minwidth=25)
todoTable.column("Description", anchor=tk.W, width=300, minwidth=100)
todoTable.heading("Task", text="Task", anchor=tk.W)
todoTable.heading("Description", text="Description", anchor=tk.W)

for todo in fetchTodos():
    todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(
        todo["title"], todo["body"]))

todoTable.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)


# Delete Todo button
def removeTodo():
    id = todoTable.focus()
    if id:
        todoTable.delete(id)
        deleteTodo(id)


removeTodoBtn = ctk.CTkButton(
    root, text="Delete Task", command=removeTodo, fg_color="#A80E11", hover_color="#8B0D0D")

removeTodoBtn.pack(pady=(0, 20))


# Edit/Add Todo region
addTodoFrame = ctk.CTkFrame(root)
addTodoFrame.pack(pady=20)

titleLabel = ctk.CTkLabel(addTodoFrame, text="Title")
titleLabel.grid(row=0, column=0, padx=150)
titleInput = ctk.CTkEntry(addTodoFrame)
titleInput.grid(row=1, column=0)


descriptionLabel = ctk.CTkLabel(addTodoFrame, text="Description")
descriptionLabel.grid(row=2, column=0)
descriptionInput = ctk.CTkTextbox(addTodoFrame)
descriptionInput.grid(row=3, column=0, pady=(0, 15))


# Add and Update Todos Region
def addTodo():
  if not titleInput.get().strip() and not descriptionInput.get("1.0", "end-1c").strip():
    return

  todo = postTodo({"title": titleInput.get(),
                  "body": descriptionInput.get("1.0", "end-1c")})
  todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(
      todo["title"], todo["body"]))
  titleInput.delete(0, tk.END)
  descriptionInput.delete("1.0", tk.END)


addTodoBtn = ctk.CTkButton(root, text="Add Task", command=addTodo)
addTodoBtn.pack(pady=(0, 20))


root.mainloop()
