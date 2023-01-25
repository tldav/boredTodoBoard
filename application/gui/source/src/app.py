import tkinter as tk
import customtkinter as ctk
import requests as api
import json
from tkinter import ttk

##### API

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
    res = api.post(url = API_URL, json = reqBody)
    return json.loads(res.text)
  except Exception as e:
    print(e)


##### TKInter initialization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.winfo_toplevel().title("Bored Todo Board")
root.geometry("800x800")

##### Todos Display region
todoTable = ttk.Treeview(root)
todoTable["show"] = "headings" # hides default first column
todoTable['columns'] = ("Todo", "Description")

todoTable.column("Todo", anchor=tk.W, width=150, minwidth=25)
todoTable.column("Description", anchor=tk.W, width=250, minwidth=25)
todoTable.heading("Todo", text="Todo", anchor=tk.W)
todoTable.heading("Description", text="Description", anchor=tk.W)

for todo in fetchTodos():
  todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(todo["title"], todo["body"]))

todoTable.pack(pady=20)

##### Edit/Add Todo region
addTodoFrame = ctk.CTkFrame(root)
addTodoFrame.pack(pady=20)

titleLabel = ctk.CTkLabel(addTodoFrame, text="Title")
titleLabel.grid(row=0, column=0, padx=150)
# titleLabel.grid(sticky="W", row=0, column=0, padx=150)
# titleLabel.grid_rowconfigure(0, weight=1)
# titleLabel.grid_columnconfigure(0, weight=1)

titleInput = ctk.CTkEntry(addTodoFrame)
titleInput.grid(row=1, column=0)
# titleInput.grid(sticky="W", row=1, column=0)
# titleInput.grid_rowconfigure(0, weight=1)
# titleInput.grid_columnconfigure(0, weight=1)

descriptionLabel = ctk.CTkLabel(addTodoFrame, text="Description")
descriptionLabel.grid(row=2, column=0)
# descriptionLabel.grid_rowconfigure(0, weight=1)
# descriptionLabel.grid_columnconfigure(0, weight=1)

descriptionInput = ctk.CTkTextbox(addTodoFrame)
descriptionInput.grid(row=3, column=0, pady=(0, 15))
# descriptionInput.grid(stick="W", row=3, column=0, pady=(0, 15))
# descriptionInput.grid_rowconfigure(0, weight=1)
# descriptionInput.grid_columnconfigure(0, weight=1)


#### Add and Update Todos Region
def addTodo():
  todo = postTodo({"title": titleInput.get(), "body": descriptionInput.get("1.0", "end-1c")})
  todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(todo["title"], todo["body"]))
  titleInput.delete(0, tk.END)
  descriptionInput.delete("1.0", tk.END)


##### 
addTodo = ctk.CTkButton(root, text="Add Todo", command=addTodo)
addTodo.pack(pady=20)


root.mainloop()