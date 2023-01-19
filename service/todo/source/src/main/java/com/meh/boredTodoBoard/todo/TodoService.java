package com.meh.boredTodoBoard.todo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@SuppressWarnings("unused")
@Service
public class TodoService {
    @Autowired
    private TodoRepository todoRepository;
    
    @SuppressWarnings("Convert2MethodRef")
    public List<Todo> getAllTodos() {
        List<Todo> todos = new ArrayList<>();
        this.todoRepository.findAll().forEach(todo -> todos.add(todo));
        return todos;
    }
    
    public Todo getTodo(Long id) {
        return this.todoRepository.findById(id).orElse(null);
    }
    
    public void addTodo(Todo todo) {
        this.todoRepository.save(todo);
    }
}
