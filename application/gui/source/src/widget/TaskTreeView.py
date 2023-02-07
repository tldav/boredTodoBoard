from tkinter import ttk
import tkinter as tk

class TaskTreeView(ttk.Treeview):
  def __init__(self, parent):
    super().__init__(parent)
    
    self["show"] = "headings"  # hides default first column
    self['columns'] = ("Task", "Description")
    self.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)

    self.column("Task", anchor=tk.W, width=75, minwidth=25)
    self.column("Description", anchor=tk.W, width=300, minwidth=100)
    self.heading("Task", text="Task", anchor=tk.W)
    self.heading("Description", text="Description", anchor=tk.W)
