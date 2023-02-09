import requests as req
import json

# API
API_URL = "http://localhost:8000/todo"

def fetchTodos():
  try:
    res = req.get(API_URL)
    todos = json.loads(res.text)
    return todos
  except Exception as e:
    print(e)

def postTodo(todo):
  reqBody = {
    "title": todo["title"],
    "body": todo["body"]
  }
  try:
    res = req.post(url=API_URL, json=reqBody)
    return json.loads(res.text)
  except Exception as e:
    print(e)

def putTodo(id, todo):
  url = "{}/{}".format(API_URL, id)
  reqBody = {
    "title": todo["title"],
    "body": todo["body"]
  }
  try:
    res = req.put(url=url, json=reqBody)
    return json.loads(res.text)
  except Exception as e:
    print(e)

def deleteTodo(id):
  url = "{}/{}".format(API_URL, id)
  try:
    req.delete(url)
  except Exception as e:
    print(e)