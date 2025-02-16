package com.example.emergency_response.services;

import com.example.emergency_response.models.Prediction;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PredictionService {

    private final RestTemplate restTemplate;

    @Value("${fastapi.url}")
    private String fastApiUrl; // Set this in application.properties

    public PredictionService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public Prediction getPrediction(Prediction predictionInput) {
        String url = fastApiUrl + "/predict";
        return restTemplate.postForObject(url, predictionInput, Prediction.class);
    }
}
