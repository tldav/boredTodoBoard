package com.meh.boredTodoBoard.todo;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Todo {
    
    @Id
    @GeneratedValue
    private Long id;
    private String title;
    private String body;
    
    public Todo() {
    }
    
    public Todo(Long id, String title, String body) {
        this.id = id;
        this.title = title;
        this.body = body;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getTitle() {
        return title;
    }
    
    public void setTitle(String title) {
        this.title = title;
    }
    
    public String getBody() {
        return body;
    }
    
    public void setBody(String body) {
        this.body = body;
    }
}
