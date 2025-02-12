package com.example.emergency_response.models;

import jakarta.persistence.*;

import java.time.LocalDateTime;
@Entity  // Marks this as a JPA entity (maps to a database table)
@Table(name = "emergencies")  // Sets table name in the database

public class Emergency {

    @Id  // Primary Key
    @GeneratedValue(strategy = GenerationType.IDENTITY)  // Auto-increment
    private Long id;

    @Column(nullable = false)  // Not null
    private String type;

    @Column(nullable = false)
    private String location;

    @Column(nullable = false)
    private String severity;

    @Column(nullable = false)
    private LocalDateTime timestamp;

    // Constructors
    public Emergency() {}

    public Emergency(String type, String location, String severity, LocalDateTime timestamp) {
        this.type = type;
        this.location = location;
        this.severity = severity;
        this.timestamp = timestamp;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}