# Plant-Recommenders
Recommends plants based on indoor air pollutant concentrations
# 🌿 Automated Plant Recommendation Engine

## Overview
This Python-based tool acts as a decision support system for indoor air quality management. It simulates a control loop that:
1.  **Ingests** raw sensor data (Temperature, CO2, Humidity, TVOC).
2.  **Diagnoses** environmental severity based on safety thresholds.
3.  **Filters** a database of biological solutions (plants) to find specific remediation candidates.
4.  **Respects** user constraints (Light availability, Safety requirements).

## Technical Implementation
* **Language:** Python 3.x
* **Key Concepts:** Dictionary Data Structures, Conditional Logic, Data Filtering.
* **Logic Flow:** `Sensor Input` -> `Severity Calculation` -> `Constraint Filtering` -> `Recommendation`

## How to Run
1.  Download the script `plant_recommender.py`.
2.  Run in terminal: `python plant_recommender.py`
3.  Enter sensor values when prompted.

## Example Output
```text
--- DIAGNOSIS ---
Status: {'co2': 'high', 'tvoc': 'ok', 'heat': 'high', 'hum': 'high'}

--- SOLUTIONS ---
[Problem: co2 is high]
  Recommended: ['Snake Plant']
