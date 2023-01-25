package com.meh.boredTodoBoard.todo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class TodoController {
    @Autowired
    private TodoService todoService;
    
    @RequestMapping("/todo")
    public List<Todo> getAllTodos() {
        return this.todoService.getAllTodos();
    }
    
    @RequestMapping("/todo/{id}")
    public Todo getTodo(@PathVariable Long id) {
        return this.todoService.getTodo(id);
    }
    
    @RequestMapping(method = RequestMethod.POST, value = "/todo")
    public Todo addTodo(@RequestBody Todo todo) {
        this.todoService.addTodo(todo);
        return todo;
    }
    
    @RequestMapping(method = RequestMethod.PUT, value = "/todo/{id}")
    public void updateTodo(@PathVariable Long id, @RequestBody Todo todo) {
        this.todoService.updateTodo(id, todo);
    }
    
    @RequestMapping(method = RequestMethod.DELETE, value = "/todo/{id}")
    public void deleteTodo(@PathVariable Long id) {
        this.todoService.deleteTodo(id);
    }
}
