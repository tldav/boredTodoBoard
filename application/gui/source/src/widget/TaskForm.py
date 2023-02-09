import customtkinter as ctk
import service.todo as api

class TaskForm(ctk.CTkFrame):
  def __init__(self, parent, isUpdate):
    self.isUpdate = isUpdate
    self.parent = parent
    self.taskId = parent.treeview.focus()
    super().__init__(parent)

    self.pack(fill="none", expand=True)

    titleLabel = ctk.CTkLabel(self, text="Title")
    titleLabel.grid(row=0, column=0, padx=150)
    titleInput = ctk.CTkEntry(self)
    titleInput.grid(row=1, column=0)

    descriptionLabel = ctk.CTkLabel(self, text="Description")
    descriptionLabel.grid(row=2, column=0)
    descriptionInput = ctk.CTkTextbox(self)
    descriptionInput.grid(row=3, column=0, pady=(0, 15))

    if (self.isUpdate):
      titleInput.insert(0, parent.treeview.item(self.taskId).get("values")[0])
      descriptionInput.insert("insert", parent.treeview.item(self.taskId).get("values")[1])

  def addTask(self):
    titleInput = self.winfo_children()[1]
    descriptionInput = self.winfo_children()[3]
    if not titleInput.get().strip() and not descriptionInput.get("1.0", "end-1c").strip():
      return
    task = api.postTodo({"title": titleInput.get(), "body": descriptionInput.get("1.0", "end-1c")})
    self.parent.treeview.insertTask(task["id"], task["title"], task["body"])
    self.parent.destroy()

  def updateTask(self):
    titleInput = self.winfo_children()[1]
    descriptionInput = self.winfo_children()[3]
    if not titleInput.get().strip() and not descriptionInput.get("1.0", "end-1c").strip():
      return
    task = api.putTodo(self.taskId, {"title": titleInput.get(), "body": descriptionInput.get("1.0", "end-1c")})
    self.parent.treeview.item(self.taskId, text="", values=(task["title"], task["body"]))
    self.parent.destroy()
