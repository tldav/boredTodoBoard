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
style.apply(root)

taskTreeView = TaskTreeView(root)

def onDoubleClick(event):
  regionClicked = taskTreeView.identify_region(event.x, event.y)
  if (regionClicked not in ("cell")):
    return
  windowName = "Edit Task: " + taskTreeView.item(taskTreeView.focus()).get("values")[0]
  editTaskWindow = TaskTopLevel(root, taskTreeView, windowName)
  form = TaskForm(editTaskWindow, True)
  editTaskBtn = ctk.CTkButton(editTaskWindow, text="Update Task", command=form.updateTask)
  editTaskBtn.pack(pady=(0, 20))

taskTreeView.bind("<Double-1>", onDoubleClick)

def openAddTaskForm():
  addTaskWindow = TaskTopLevel(root, taskTreeView, "New Task")
  form = TaskForm(addTaskWindow, False)
  addTaskBtn = ctk.CTkButton(addTaskWindow, text="Add Task", command=form.addTask)
  addTaskBtn.pack(pady=(0, 20))

removeTaskBtn = ctk.CTkButton(
    root, text="Delete Task", command=taskTreeView.removeTask, fg_color="#A80E11", hover_color="#8B0D0D")
openAddTaskBtn = ctk.CTkButton(root, text="New Task", command=openAddTaskForm)
openAddTaskBtn.pack( pady=(20, 20))
removeTaskBtn.pack(pady=(0, 60))

root.mainloop()