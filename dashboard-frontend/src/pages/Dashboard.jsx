import React, { useEffect, useState } from "react";
import axios from "axios";
import { Bar, Line } from "react-chartjs-2";
import "chart.js/auto";
import "../styles/Dashboard.css";

const Dashboard = () => {
    const [data, setData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);
    const [totalDisasters, setTotalDisasters] = useState(0);
    const [totalDeaths, setTotalDeaths] = useState(0);
    const [mostAffectedRegion, setMostAffectedRegion] = useState("N/A");
    const [monthlyData, setMonthlyData] = useState([]);
    const [deathsData, setDeathsData] = useState([]);

    // Filter states
    const [selectedSubGroup, setSelectedSubGroup] = useState("All");
    const [selectedType, setSelectedType] = useState("All");
    const [selectedRegion, setSelectedRegion] = useState("All");

    useEffect(() => {
        axios.get("http://localhost:8080/api/emergencies")
            .then(response => {
                setData(response.data);
                setFilteredData(response.data);
                processData(response.data);
            })
            .catch(error => console.error("Error fetching data:", error));
    }, []);

    const processData = (emergencies) => {
        setTotalDisasters(emergencies.length);
        setTotalDeaths(emergencies.reduce((sum, e) => sum + (e.totalDeaths || 0), 0));

        // Find the most affected sub-region
        const subRegionCount = emergencies.reduce((acc, curr) => {
            acc[curr.subRegion] = (acc[curr.subRegion] || 0) + 1;
            return acc;
        }, {});
        
        const mostAffected = Object.keys(subRegionCount).reduce((a, b) =>
            subRegionCount[a] > subRegionCount[b] ? a : b, "N/A");
        
        setMostAffectedRegion(mostAffected);

        // Monthly disasters and deaths data
        const monthCounts = Array(12).fill(0);
        const deathsCounts = Array(12).fill(0);

        emergencies.forEach(e => {
            let startMonth = e.startMonth >= 1 && e.startMonth <= 12 ? e.startMonth - 1 : null;
            let endMonth = e.endMonth >= 1 && e.endMonth <= 12 ? e.endMonth - 1 : startMonth;

            if (startMonth !== null) {
                for (let m = startMonth; m <= endMonth; m++) {
                    monthCounts[m]++;
                    deathsCounts[m] += e.totalDeaths || 0;
                }
            }
        });

        setMonthlyData(monthCounts);
        setDeathsData(deathsCounts);
    };

    const applyFilters = () => {
        let filtered = data;
        if (selectedSubGroup !== "All") {
            filtered = filtered.filter(e => e.disasterSubGroup === selectedSubGroup);
        }
        if (selectedType !== "All") {
            filtered = filtered.filter(e => e.disasterType === selectedType);
        }
        if (selectedRegion !== "All") {
            filtered = filtered.filter(e => e.subRegion === selectedRegion);
        }

        setFilteredData(filtered);
        processData(filtered);
    };

    return (
        <div className="dashboard-container">
            {/* Sidebar */}
            <div className="sidebar">
                <h2>Emergency Dashboard</h2>
                <a href="#" className="active">Reports</a>
                <a href="#">Library</a>
                <a href="#">People</a>
                <a href="#">Settings</a>
            </div>

            {/* Main content */}
            <div className="main-content">
                <h2 className="dashboard-header">Reports</h2>

                {/* Filters */}
                <div className="filters">
                    <select value={selectedSubGroup} onChange={(e) => setSelectedSubGroup(e.target.value)}>
                        <option value="All">All Disaster Sub-Groups</option>
                        {[...new Set(data.map(e => e.disasterSubGroup))].map(sub => (
                            <option key={sub} value={sub}>{sub}</option>
                        ))}
                    </select>
                    <select value={selectedType} onChange={(e) => setSelectedType(e.target.value)}>
                        <option value="All">All Disaster Types</option>
                        {[...new Set(data.map(e => e.disasterType))].map(type => (
                            <option key={type} value={type}>{type}</option>
                        ))}
                    </select>
                    <select value={selectedRegion} onChange={(e) => setSelectedRegion(e.target.value)}>
                        <option value="All">All Regions</option>
                        {[...new Set(data.map(e => e.subRegion))].map(region => (
                            <option key={region} value={region}>{region}</option>
                        ))}
                    </select>
                    <button onClick={applyFilters}>Apply Filters</button>
                </div>

                {/* Summary cards */}
                <div className="cards">
                    <div className="card">
                        <h3>Total Disasters</h3>
                        <p>{totalDisasters}</p>
                    </div>
                    <div className="card">
                        <h3>Most Affected Region</h3>
                        <p>{mostAffectedRegion}</p>
                    </div>
                    <div className="card">
                        <h3>Total Deaths</h3>
                        <p>{totalDeaths}</p>
                    </div>
                </div>

                {/* Charts */}
                <div className="chart-container">
                    <h3>Disasters Reported Per Month</h3>
                    <Bar
                        data={{
                            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                            datasets: [{
                                label: "Disasters Reported",
                                data: monthlyData,
                                backgroundColor: "#3b82f6",
                            }]
                        }}
                    />
                </div>

                <div className="chart-container">
                    <h3>Total Deaths Per Month</h3>
                    <Line
                        data={{
                            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                            datasets: [{
                                label: "Total Deaths",
                                data: deathsData,
                                borderColor: "#ef4444",
                                backgroundColor: "rgba(239, 68, 68, 0.2)",
                                fill: true
                            }]
                        }}
                    />
                </div>
            </div>
        </div>
    );
};

export default Dashboard;