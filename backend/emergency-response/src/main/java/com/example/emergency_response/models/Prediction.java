package com.example.emergency_response.models;

public class Prediction {
    private String disasterType;
    private String subRegion;
    private double magnitude;
    private int noAffected;

    // Output fields from FastAPI
    private int predictedStartYear;
    private int predictedStartMonth;
    private int predictedTotalDeaths;
    private int predictedNoAffected;
    private int predictedNoHomeless;
    private int predictedNoInjured;

    // Constructors
    public Prediction() {}

    public Prediction(String disasterType, String subRegion, double magnitude, int noAffected) {
        this.disasterType = disasterType;
        this.subRegion = subRegion;
        this.magnitude = magnitude;
        this.noAffected = noAffected;
    }

    // Getters and Setters
    public String getDisasterType() { return disasterType; }
    public void setDisasterType(String disasterType) { this.disasterType = disasterType; }

    public String getSubRegion() { return subRegion; }
    public void setSubRegion(String subRegion) { this.subRegion = subRegion; }

    public double getMagnitude() { return magnitude; }
    public void setMagnitude(double magnitude) { this.magnitude = magnitude; }

    public int getNoAffected() { return noAffected; }
    public void setNoAffected(int noAffected) { this.noAffected = noAffected; }

    public int getPredictedStartYear() { return predictedStartYear; }
    public void setPredictedStartYear(int predictedStartYear) { this.predictedStartYear = predictedStartYear; }

    public int getPredictedStartMonth() { return predictedStartMonth; }
    public void setPredictedStartMonth(int predictedStartMonth) { this.predictedStartMonth = predictedStartMonth; }

    public int getPredictedTotalDeaths() { return predictedTotalDeaths; }
    public void setPredictedTotalDeaths(int predictedTotalDeaths) { this.predictedTotalDeaths = predictedTotalDeaths; }

    public int getPredictedNoAffected() { return predictedNoAffected; }
    public void setPredictedNoAffected(int predictedNoAffected) { this.predictedNoAffected = predictedNoAffected; }

    public int getPredictedNoHomeless() { return predictedNoHomeless; }
    public void setPredictedNoHomeless(int predictedNoHomeless) { this.predictedNoHomeless = predictedNoHomeless; }

    public int getPredictedNoInjured() { return predictedNoInjured; }
    public void setPredictedNoInjured(int predictedNoInjured) { this.predictedNoInjured = predictedNoInjured; }
}
