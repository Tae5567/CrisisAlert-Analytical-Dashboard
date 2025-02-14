package com.example.emergency_response.models;

import jakarta.persistence.*;

@Entity
@Table(name = "emergencies")
public class Emergency {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String disasterType;

    @Column(nullable = false)
    private String disasterGroup;

    @Column(nullable = false)
    private String disasterSubGroup;

    @Column(nullable = false)
    private String country;

    @Column(nullable = false)
    private String region;

    @Column(nullable = false)
    private String subRegion;

    @Column
    private Integer totalDeaths;

    @Column
    private Integer noInjured;

    @Column
    private Integer noAffected;

    @Column
    private Integer noHomeless;

    @Column
    private Double magnitude;

    @Column(nullable = false)
    private Integer startYear;

    @Column(nullable = false)
    private Integer startMonth;

    @Column
    private Integer endYear;

    @Column
    private Integer endMonth;

    // Constructors
    public Emergency() {}

    public Emergency(String disasterType, String disasterGroup, String disasterSubGroup, String country, 
                     String region, String subRegion, Integer totalDeaths, Integer noInjured, 
                     Integer noAffected, Integer noHomeless, Double magnitude, 
                     Integer startYear, Integer startMonth, Integer endYear, Integer endMonth) {
        this.disasterType = disasterType;
        this.disasterGroup = disasterGroup;
        this.disasterSubGroup = disasterSubGroup;
        this.country = country;
        this.region = region;
        this.subRegion = subRegion;
        this.totalDeaths = totalDeaths;
        this.noInjured = noInjured;
        this.noAffected = noAffected;
        this.noHomeless = noHomeless;
        this.magnitude = magnitude;
        this.startYear = startYear;
        this.startMonth = startMonth;
        this.endYear = endYear;
        this.endMonth = endMonth;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getDisasterType() { return disasterType; }
    public void setDisasterType(String disasterType) { this.disasterType = disasterType; }

    public String getDisasterGroup() { return disasterGroup; }
    public void setDisasterGroup(String disasterGroup) { this.disasterGroup = disasterGroup; }

    public String getDisasterSubGroup() { return disasterSubGroup; }
    public void setDisasterSubGroup(String disasterSubGroup) { this.disasterSubGroup = disasterSubGroup; }

    public String getCountry() { return country; }
    public void setCountry(String country) { this.country = country; }

    public String getRegion() { return region; }
    public void setRegion(String region) { this.region = region; }

    public String getSubRegion() { return subRegion; }
    public void setSubRegion(String subRegion) { this.subRegion = subRegion; }

    public Integer getTotalDeaths() { return totalDeaths; }
    public void setTotalDeaths(Integer totalDeaths) { this.totalDeaths = totalDeaths; }

    public Integer getNoInjured() { return noInjured; }
    public void setNoInjured(Integer noInjured) { this.noInjured = noInjured; }

    public Integer getNoAffected() { return noAffected; }
    public void setNoAffected(Integer noAffected) { this.noAffected = noAffected; }

    public Integer getNoHomeless() { return noHomeless; }
    public void setNoHomeless(Integer noHomeless) { this.noHomeless = noHomeless; }

    public Double getMagnitude() { return magnitude; }
    public void setMagnitude(Double magnitude) { this.magnitude = magnitude; }

    public Integer getStartYear() { return startYear; }
    public void setStartYear(Integer startYear) { this.startYear = startYear; }

    public Integer getStartMonth() { return startMonth; }
    public void setStartMonth(Integer startMonth) { this.startMonth = startMonth; }

    public Integer getEndYear() { return endYear; }
    public void setEndYear(Integer endYear) { this.endYear = endYear; }

    public Integer getEndMonth() { return endMonth; }
    public void setEndMonth(Integer endMonth) { this.endMonth = endMonth; }
}