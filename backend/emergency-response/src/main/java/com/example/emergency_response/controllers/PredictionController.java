package com.example.emergency_response.controllers;

import com.example.emergency_response.models.Prediction;
import com.example.emergency_response.services.PredictionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/predict")
public class PredictionController {

    private final PredictionService predictionService;

    @Autowired
    public PredictionController(PredictionService predictionService) {
        this.predictionService = predictionService;
    }

    @PostMapping
    public Prediction predictDisaster(@RequestBody Prediction predictionInput) {
        return predictionService.getPrediction(predictionInput);
    }
}