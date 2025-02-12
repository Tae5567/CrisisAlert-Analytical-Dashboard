package com.example.emergency_response.services;

import com.example.emergency_response.models.Emergency;
import com.example.emergency_response.repositories.EmergencyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class EmergencyService {

    @Autowired
    private EmergencyRepository emergencyRepository;

    // Fetch all emergencies
    public List<Emergency> getAllEmergencies() {
        return emergencyRepository.findAll();
    }

    // Fetch a single emergency by ID
    public Optional<Emergency> getEmergencyById(Long id) {
        return emergencyRepository.findById(id);
    }

    // Save a new emergency
    public Emergency saveEmergency(Emergency emergency) {
        return emergencyRepository.save(emergency);
    }

    // Delete an emergency by ID
    public void deleteEmergency(Long id) {
        emergencyRepository.deleteById(id);
    }
}