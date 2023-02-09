import tkinter as tk
import customtkinter as ctk
import style.style as style
from widget.TaskTreeView import TaskTreeView
from widget.TaskForm import TaskForm
from window.TaskTopLevel import TaskTopLevel

# TKInter initialization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.title("Bored Todo Board")
root.geometry("800x800")
# Style
style.apply(root)


todoTable = TaskTreeView(root)



# Double Click in Todo Region
def onDoubleClick(event):
  regionClicked = todoTable.identify_region(event.x, event.y)
  if (regionClicked not in ("cell")):
    return

  column = todoTable.identify_column(event.x)
  columnIndex = int(column[1:]) - 1

  selectedId = todoTable.focus()
  selectedText = todoTable.item(selectedId).get("values")[columnIndex]

  print(todoTable.selection())
  columnBox = todoTable.bbox(selectedId, column)

  windowName = "Edit Task: " + todoTable.item(selectedId).get("values")[0]

  editTodoWindow = TaskTopLevel(root, todoTable, windowName)

  form = TaskForm(editTodoWindow, True)

  editTodoBtn = ctk.CTkButton(editTodoWindow, text="Update Task", command=form.updateTask)
  editTodoBtn.pack(pady=(0, 20))


todoTable.bind("<Double-1>", onDoubleClick)

removeTodoBtn = ctk.CTkButton(
    root, text="Delete Task", command=todoTable.removeTask, fg_color="#A80E11", hover_color="#8B0D0D")

removeTodoBtn.pack(pady=(0, 20))

def openAddTaskForm():
  addTodoWindow = TaskTopLevel(root, todoTable, "New Task")
  form = TaskForm(addTodoWindow, False)
  addTaskBtn = ctk.CTkButton(addTodoWindow, text="Add Task", command=form.addTask)
  addTaskBtn.pack(pady=(0, 20))
  

openAddTaskBtn = ctk.CTkButton(root, text="New Task", command=openAddTaskForm)

# Render add todo button
openAddTaskBtn.pack(pady=(0, 20))


root.mainloop()
