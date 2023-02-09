import customtkinter as ctk

class TaskTopLevel(ctk.CTkToplevel):
  def __init__(self, parent, treeview, windowName):
    self.treeview = treeview
    self.windowName = windowName
    super().__init__(parent)

    self.title(windowName)
    self.geometry("400x400")
    self.wait_visibility()
    self.grab_set()