import tkinter as tk
import customtkinter as ctk
import requests as req
import json
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.winfo_toplevel().title("Bored Todo Board")
root.geometry("800x800")

table = ttk.Treeview(root)
table["show"] = "headings" # hides default first column

table['columns'] = ("Todo", "Description")

try:
  res = req.get("http://localhost:8000/todo")
  todos = json.loads(res.text)
except Exception as e:
  print(e)

# table.column("#0", width=0, minwidth=0)
table.column("Todo", anchor=tk.W, width=150, minwidth=25)
table.column("Description", anchor=tk.W, width=250, minwidth=25)

# table.heading("#0", text="", anchor=tk.W)
table.heading("Todo", text="Todo", anchor=tk.W)
table.heading("Description", text="Description", anchor=tk.W)

for todo in todos:
  table.insert(parent="", index="end", iid=todo["id"], text="", values=(todo["title"], todo["body"]))

table.pack(pady=20)


root.mainloop()