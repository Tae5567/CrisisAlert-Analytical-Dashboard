import React, { useState } from "react";
import axios from "axios";
import "../styles/Dashboard.css"; // Ensure your main styles are imported

const Prediction = () => {
    const [disasterType, setDisasterType] = useState("");
    const [subRegion, setSubRegion] = useState("");
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState("");

    // Dropdown options
    const disasterTypes = [
        "Flood", "Drought", "Earthquake", "Storm", "Landslide",
        "Wildfire", "Volcanic Activity", "Extreme Temperature"
    ];

    const subRegions = ["Sub-Saharan Africa", "Northern Africa"];

    // Handle Prediction Request
    const handlePredict = async () => {
        console.log("Sending payload:", { disaster_type: disasterType, sub_region: subRegion });
        try {
            const response = await axios.post("http://localhost:8000/predict", {
                disaster_type: disasterType,
                sub_region: subRegion,
            });
            console.log("Prediction response:", response.data);
            setPrediction(response.data);
            setError("");
        } catch (err) {
            console.error("Error fetching prediction:", err);
            setError("Failed to get prediction. Please try again.");
        }
    };
    

    return (
        <div className="dashboard-container">
            <div className="sidebar">
                <h2>Emergency Dashboard</h2>
                <a href="/dashboard">Reports</a>
                <a href="#" className="active">Predictions</a>
                <a href="#">Library</a>
                <a href="#">People</a>
                <a href="#">Settings</a>
            </div>

            <div className="main-content">
                <h2 className="dashboard-header">Disaster Predictions</h2>

                {/* Prediction Form */}
                <div className="form-container">
                    <label className="form-label">
                        Disaster Type:
                        <select
                            className="dropdown"
                            value={disasterType}
                            onChange={(e) => setDisasterType(e.target.value)}
                        >
                            <option value="">Select Disaster Type</option>
                            {disasterTypes.map((type, index) => (
                                <option key={index} value={type}>{type}</option>
                            ))}
                        </select>
                    </label>

                    <label className="form-label">
                        Sub-Region:
                        <select
                            className="dropdown"
                            value={subRegion}
                            onChange={(e) => setSubRegion(e.target.value)}
                        >
                            <option value="">Select Sub-Region</option>
                            {subRegions.map((region, index) => (
                                <option key={index} value={region}>{region}</option>
                            ))}
                        </select>
                    </label>

                    <button
                        className="predict-button"
                        onClick={handlePredict}
                        disabled={!disasterType || !subRegion}
                    >
                        Predict
                    </button>
                </div>

                {/* Error Message */}
                {error && <p className="error-message">{error}</p>}

                {/* Prediction Results */}
                {prediction && (
                    <div className="cards">
                        <div className="card"><h3>Predicted Start Year</h3><p>{prediction.predicted_start_year}</p></div>
                        <div className="card"><h3>Predicted Start Month</h3><p>{prediction.predicted_start_month}</p></div>
                        <div className="card"><h3>Predicted End Year</h3><p>{prediction.predicted_end_year}</p></div>
                        <div className="card"><h3>Predicted End Month</h3><p>{prediction.predicted_end_month}</p></div>
                        <div className="card"><h3>Predicted Total Deaths</h3><p>{prediction.predicted_total_deaths}</p></div>
                        <div className="card"><h3>Predicted Number Affected</h3><p>{prediction.predicted_no_affected}</p></div>
                        <div className="card"><h3>Predicted Number Homeless</h3><p>{prediction.predicted_no_homeless}</p></div>
                        <div className="card"><h3>Predicted Number Injured</h3><p>{prediction.predicted_no_injured}</p></div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Prediction;