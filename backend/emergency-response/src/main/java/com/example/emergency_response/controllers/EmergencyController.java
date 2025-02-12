package com.example.emergency_response.controllers;

import com.example.emergency_response.models.Emergency;
import com.example.emergency_response.services.EmergencyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/emergencies")  // Base API path
public class EmergencyController {
    
    @Autowired
    private EmergencyService emergencyService;

    // Get all emergencies
    @GetMapping
    public List<Emergency> getAllEmergencies() {
        return emergencyService.getAllEmergencies();
    }

    // Get an emergency by ID
    @GetMapping("/{id}")
    public Optional<Emergency> getEmergencyById(@PathVariable Long id) {
        return emergencyService.getEmergencyById(id);
    }

    // Create a new emergency
    @PostMapping
    public Emergency createEmergency(@RequestBody Emergency emergency) {
        return emergencyService.saveEmergency(emergency);
    }

    // Delete an emergency by ID
    @DeleteMapping("/{id}")
    public void deleteEmergency(@PathVariable Long id) {
        emergencyService.deleteEmergency(id);
    }
}
