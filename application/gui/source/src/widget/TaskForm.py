import customtkinter as ctk

class TaskForm(ctk.CTkFrame):
  def __init__(self, parent):
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