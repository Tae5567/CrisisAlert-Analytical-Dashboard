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

    // Get all emergencies
    public List<Emergency> getAllEmergencies() {
        return emergencyRepository.findAll();
    }

    // Get an emergency by ID
    public Optional<Emergency> getEmergencyById(Long id) {
        return emergencyRepository.findById(id);
    }

    // Add a new emergency
    public Emergency addEmergency(Emergency emergency) {
        return emergencyRepository.save(emergency);
    }

    // Update an existing emergency
    public Emergency updateEmergency(Long id, Emergency updatedEmergency) {
        return emergencyRepository.findById(id).map(emergency -> {
            emergency.setDisasterType(updatedEmergency.getDisasterType());
            emergency.setDisasterGroup(updatedEmergency.getDisasterGroup());
            emergency.setDisasterSubGroup(updatedEmergency.getDisasterSubGroup());
            emergency.setCountry(updatedEmergency.getCountry());
            emergency.setRegion(updatedEmergency.getRegion());
            emergency.setSubRegion(updatedEmergency.getSubRegion());
            emergency.setTotalDeaths(updatedEmergency.getTotalDeaths());
            emergency.setNoInjured(updatedEmergency.getNoInjured());
            emergency.setNoAffected(updatedEmergency.getNoAffected());
            emergency.setNoHomeless(updatedEmergency.getNoHomeless());
            emergency.setMagnitude(updatedEmergency.getMagnitude());
            emergency.setStartYear(updatedEmergency.getStartYear());
            emergency.setStartMonth(updatedEmergency.getStartMonth());
            emergency.setEndYear(updatedEmergency.getEndYear());
            emergency.setEndMonth(updatedEmergency.getEndMonth());

            return emergencyRepository.save(emergency);
        }).orElseThrow(() -> new RuntimeException("Emergency not found"));
    }

    // Delete an emergency by ID
    public void deleteEmergency(Long id) {
        emergencyRepository.deleteById(id);
    }
}