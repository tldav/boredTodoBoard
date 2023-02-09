from tkinter import ttk
import service.todo as api

class TaskTreeView(ttk.Treeview):
  def __init__(self, parent):
    taskList = api.fetchTodos()
    super().__init__(parent)  
    
    self["show"] = "headings"
    self['columns'] = ("Task", "Description")
    self.pack(pady=20, padx=40, fill="both", expand=True)

    self.column("Task", anchor="w", width=75, minwidth=25)
    self.column("Description", anchor="w", width=300, minwidth=100)
    self.heading("Task", text="Task", anchor="w")
    self.heading("Description", text="Description", anchor="w")

    for task in taskList:
      self.insertTask(task["id"], task["title"], task["body"])

  def insertTask(self, id, title, body):
    self.insert(parent="", index="end", iid=id, text="", values=(title, body))

  def removeTask(self):
    id = self.focus()
    if id:
      self.delete(id)
      api.deleteTodo(id)





  # def createTask(self, titleInput, descInput):
  #   if not titleInput.get().strip() and not descInput.get("1.0", "end-1c").strip():
  #     return

  #   todo = api.postTodo({"title": titleInput.get(), "body": descInput.get("1.0", "end-1c")})

  #   self.__insertTask(todo["id"], todo["title"], todo["body"])

  #   titleInput.delete(0, "end")
  #   descInput.delete("1.0", "end")