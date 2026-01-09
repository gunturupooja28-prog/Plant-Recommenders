# --- 1. THE DATABASE ---
PLANT_DATA = [
    { "name": "Areca Palm", "triggers": {"heat": ['high'], "hum": ['high']}, "time": "any", "safe": True, "light_tol": ['medium', 'high'] },
    { "name": "Snake Plant", "triggers": {"heat": ['high'], "co2": ['high']}, "time": "night", "safe": False, "light_tol": ['low', 'medium'] },
    { "name": "Boston Fern", "triggers": {"hum": ['high'], "tvoc": ['high']}, "time": "any", "safe": True, "light_tol": ['medium'] },
    { "name": "Golden Pothos", "triggers": {"tvoc": ['mod'], "co2": ['mod']}, "time": "day", "safe": False, "light_tol": ['low', 'medium'] }
]

# --- 2. SEVERITY CALCULATOR ---
def calculate_severity(co2, tvoc, temp, hum):
    severity = {"co2": "ok", "tvoc": "ok", "heat": "ok", "hum": "ok"}
    
    if temp > 30: severity["heat"] = "high"
    elif temp > 25: severity["heat"] = "mod"
    else: severity["heat"] = "low"
        
    if co2 > 1500: severity["co2"] = "high"
    elif co2 > 800: severity["co2"] = "mod"
    else: severity["heat"] = "low"
        
    if hum < 30: severity["hum"] = "high"
    elif hum < 50: severity["hum"] = "mod"
    else: severity["heat"] = "low"
        
    if tvoc > 1000: severity["tvoc"] = "high"
    else: severity["heat"] = "low"
    
    return severity

# --- 3. FILTERING ENGINE ---
def filter_plants(pollutant_type, severity_level, context):
    matches = []
    for plant in PLANT_DATA:
        # Check 1: Pollutant
        if pollutant_type not in plant["triggers"]: continue
        # Check 2: Strength
        if severity_level not in plant["triggers"][pollutant_type]: continue
        # Check 3: Light
        if context["light_level"] not in plant["light_tol"]: continue
        # Check 4: Safety
        if context["pet_safe_required"] and not plant["safe"]: continue
        
        matches.append(plant["name"]) 
    return matches

# --- 4. EXECUTION

print("--- WELCOME TO THE PLANT RECOMMENDER ---")
print("Please enter the current sensor readings:")
user_temp = int(input("Temperature (C): \n"))
user_co2  = int(input("CO2 Level (ppm): \n"))
user_hum  = int(input("Humidity (%): \n"))
user_tvoc = int(input("TVOC Level (ppb): \n"))

sensors = { 
    "co2": user_co2, 
    "tvoc": user_tvoc, 
    "temp": user_temp, 
    "hum": user_hum 
}

# Hard-coded preferences for now (to keep it simple)
prefs = { "time_of_day": "night", "light_level": "medium", "pet_safe_required": False }

print(f"--- DIAGNOSIS ---")
diagnosis = calculate_severity(sensors["co2"], sensors["tvoc"], sensors["temp"], sensors["hum"])
print(f"{diagnosis}")

print(f"\n--- SOLUTIONS ---")
for pollutant, level in diagnosis.items():
    if level != "ok" or "low":
        print(f"\n[Problem: {pollutant} is {level}]")
        my_plants = filter_plants(pollutant, level, prefs)
        
        if my_plants:
            print(f"  Recommended: {my_plants}")
        else:
            print(f"  No suitable plants found.")
    else:
        print(f"The {pollutant} is under safe levels")


