package com.example.emergency_response.controllers;

import com.example.emergency_response.models.Emergency;
import com.example.emergency_response.services.EmergencyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/emergencies")
public class EmergencyController {

    @Autowired
    private EmergencyService emergencyService;

    // Get all emergencies
    @GetMapping
    public List<Emergency> getAllEmergencies() {
        return emergencyService.getAllEmergencies();
    }

    // Get emergency by ID
    @GetMapping("/{id}")
    public ResponseEntity<Emergency> getEmergencyById(@PathVariable Long id) {
        Optional<Emergency> emergency = emergencyService.getEmergencyById(id);
        return emergency.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Add a new emergency
    @PostMapping
    public ResponseEntity<Emergency> addEmergency(@RequestBody Emergency emergency) {
        Emergency savedEmergency = emergencyService.addEmergency(emergency);
        return ResponseEntity.ok(savedEmergency);
    }

    // Update an emergency
    @PutMapping("/{id}")
    public ResponseEntity<Emergency> updateEmergency(@PathVariable Long id, @RequestBody Emergency updatedEmergency) {
        try {
            Emergency emergency = emergencyService.updateEmergency(id, updatedEmergency);
            return ResponseEntity.ok(emergency);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    // Delete an emergency
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEmergency(@PathVariable Long id) {
        emergencyService.deleteEmergency(id);
        return ResponseEntity.noContent().build();
    }
}