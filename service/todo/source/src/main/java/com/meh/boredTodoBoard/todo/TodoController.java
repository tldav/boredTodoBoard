package com.meh.boredTodoBoard.todo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TodoController {
    @Autowired
    private TodoService todoService;
    
//    private final List<Todo> sample_todos = new ArrayList<>(List.of(
//            new Todo("1", "eat grass", "need to eat grass"),
//            new Todo("2", "drink goop inside lava lamp", "don't todo this"),
//            new Todo("3", "sneeze", "need to sneeze")
//    ));
    
    @RequestMapping("/todo")
    public List<Todo> getAllTopics() {
        return this.todoService.getAllTodos();
    }
    
    @RequestMapping(method = RequestMethod.POST, value = "/todo")
    public void addTodo(@RequestBody Todo todo) {
        this.todoService.addTodo(todo);
    }

}
