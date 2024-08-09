def smart_lighting(room, time_of_day):
    def morning_setting():
        return f"Setting soft morning light in {room}."

    def day_setting():
        return f"Setting bright light in {room}."

    def night_setting():
        return f"Setting dim light in {room}."

    if time_of_day == "morning":
        return morning_setting()
    elif time_of_day == "day":
        return day_setting()
    elif time_of_day == "night":
        return night_setting()


print(smart_lighting("Living Room", "morning"))
print(smart_lighting("Bedroom", "day"))
print(smart_lighting("Kitchen", "night"))
