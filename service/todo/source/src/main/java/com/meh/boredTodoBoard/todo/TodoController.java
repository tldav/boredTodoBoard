package com.meh.boredTodoBoard.todo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class TodoController {
    @Autowired
    private TodoService todoService;
    
    @RequestMapping("/todo")
    public List<Todo> getAllTopics() {
        return this.todoService.getAllTodos();
    }
    
    @RequestMapping("/todo/{id}")
    public Todo getTodo(@PathVariable Long id) {
        return this.todoService.getTodo(id);
    }
    
    @RequestMapping(method = RequestMethod.POST, value = "/todo")
    public void addTodo(@RequestBody Todo todo) {
        this.todoService.addTodo(todo);
    }

}
