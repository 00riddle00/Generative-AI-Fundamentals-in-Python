def adjust_temperature(current_temp, desired_temp):
    return f"Adjusting from {current_temp}°F to {desired_temp}°F"


thermostat_action = adjust_temperature
print(thermostat_action(68, 72))
