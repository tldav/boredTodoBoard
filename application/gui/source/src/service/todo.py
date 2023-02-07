import requests as reqs
import json

# API
API_URL = "http://localhost:8000/todo"


def fetchTodos():
    try:
        res = reqs.get(API_URL)
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
        res = reqs.post(url=API_URL, json=reqBody)
        return json.loads(res.text)
    except Exception as e:
        print(e)


def deleteTodo(id):
    url = "{}/{}".format(API_URL, id)
    try:
      reqs.delete(url)
    except Exception as e:
        print(e)