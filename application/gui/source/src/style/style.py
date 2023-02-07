from tkinter import ttk

def apply(element):
  style = ttk.Style(element)
  root(style)

def root(styleObj):
  styleObj.theme_use("clam")
  styleObj.configure("Treeview", background="#3b3b3b", foreground="white", fieldbackground="#3b3b3b")
  styleObj.configure("Treeview.Heading", background="#2b2b2b", foreground="white", font=("Roboto", 10))
  styleObj.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})
  ])