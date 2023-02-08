import tkinter as tk
import customtkinter as ctk
from widget.TaskTreeView import TaskTreeView
from widget.TaskForm import TaskForm
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

for todo in api.fetchTodos():
  todoTable.insertTask(todo["id"], todo["title"], todo["body"])
    # todoTable.insert(parent="", index="end", iid=todo["id"], text="", values=(todo["title"], todo["body"]))

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

  TaskForm(editTodoWindow)

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
  todoTable.insertTask(todo["id"], todo["title"], todo["body"])
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


# print(addTodoRegion.winfo_children())
# print("-------------------")
# print("-------------------")
# print("-------------------")
# print(addTodoRegion.children)
# print("-------------------")
# print("-------------------")
# print("-------------------")
# print(addTodoRegion.nametowidget("!ctklabel"))

# Render add todo button
addTodoBtn.pack(pady=(0, 20))


root.mainloop()
