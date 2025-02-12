package com.example.emergency_response.repositories;

import com.example.emergency_response.models.Emergency;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EmergencyRepository extends JpaRepository<Emergency, Long> {
    // to define custom queries
}
