import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from widget.TaskTreeView import TaskTreeView
import service.todo as api
import style.style as style

# TKInter initialization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.title("Bored Todo Board")
root.geometry("800x800")
# Style
style.apply(root)


todoTable = TaskTreeView(root)

# Todos Display region
# todoTable = ttk.Treeview(root)
# todoTable["show"] = "headings"  # hides default first column
# todoTable['columns'] = ("Task", "Description")

# todoTable.column("Task", anchor=tk.W, width=75, minwidth=25)
# todoTable.column("Description", anchor=tk.W, width=300, minwidth=100)
# todoTable.heading("Task", text="Task", anchor=tk.W)
# todoTable.heading("Description", text="Description", anchor=tk.W)

for todo in api.fetchTodos():
    todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(
        todo["title"], todo["body"]))

# Double Click in Todo Region
def onDoubleClick(event):
  regionClicked = todoTable.identify_region(event.x, event.y)
  if (regionClicked not in ("cell")):
    return

  column = todoTable.identify_column(event.x)
  columnIndex = int(column[1:]) - 1

  selectedId = todoTable.focus()
  selectedText = todoTable.item(selectedId).get("values")[columnIndex]
  print(todoTable.item(selectedId)) # {'text': '', 'image': '', 'values': ['yo', 'hieeeee'], 'open': 0, 'tags': ''}


  columnBox = todoTable.bbox(selectedId, column)
  print(columnBox)

  editTodoWindow = ctk.CTkToplevel(root)
  editTodoWindow.title("Edit Task: " + todoTable.item(selectedId).get("values")[0])
  editTodoWindow.geometry("400x400")

  editTodoWindow.wait_visibility()
  editTodoWindow.grab_set()
  editTodo = ctk.CTkFrame(editTodoWindow)
  editTodo.pack(fill="none", expand=True)

  titleLabel = ctk.CTkLabel(editTodo, text="Title")
  titleLabel.grid(row=0, column=0, padx=150)
  titleInput = ctk.CTkEntry(editTodo)
  titleInput.grid(row=1, column=0)


  descriptionLabel = ctk.CTkLabel(editTodo, text="Description")
  descriptionLabel.grid(row=2, column=0)
  descriptionInput = ctk.CTkTextbox(editTodo)
  descriptionInput.grid(row=3, column=0, pady=(0, 15))


  editTodoBtn = ctk.CTkButton(editTodoWindow, text="Update Task", command=print)
  editTodoBtn.pack(pady=(0, 20))




todoTable.bind("<Double-1>", onDoubleClick)


# Delete Todo
def removeTodo():
    id = todoTable.focus()
    if id:
        todoTable.delete(id)
        api.deleteTodo(id)

removeTodoBtn = ctk.CTkButton(
    root, text="Delete Task", command=removeTodo, fg_color="#A80E11", hover_color="#8B0D0D")

removeTodoBtn.pack(pady=(0, 20))



# Add Todo
def addTodo():
  if not titleInput.get().strip() and not descriptionInput.get("1.0", "end-1c").strip():
    return

  todo = api.postTodo({"title": titleInput.get(),
                  "body": descriptionInput.get("1.0", "end-1c")})
  todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(
      todo["title"], todo["body"]))
  titleInput.delete(0, tk.END)
  descriptionInput.delete("1.0", tk.END)

addTodoBtn = ctk.CTkButton(root, text="Add Task", command=addTodo)


# Edit/Add Todo region
addTodoRegion = ctk.CTkFrame(root)
addTodoRegion.pack(pady=20)

titleLabel = ctk.CTkLabel(addTodoRegion, text="Title")
titleLabel.grid(row=0, column=0, padx=150)
titleInput = ctk.CTkEntry(addTodoRegion)
titleInput.grid(row=1, column=0)


descriptionLabel = ctk.CTkLabel(addTodoRegion, text="Description")
descriptionLabel.grid(row=2, column=0)
descriptionInput = ctk.CTkTextbox(addTodoRegion)
descriptionInput.grid(row=3, column=0, pady=(0, 15))

# Render add todo button
addTodoBtn.pack(pady=(0, 20))


root.mainloop()
