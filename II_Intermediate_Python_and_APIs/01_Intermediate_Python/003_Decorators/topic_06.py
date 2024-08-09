def log_execution(original_function):
    def wrapper(*args, **kwargs):
        print("Executing smart home action...")
        original_function(*args, **kwargs)
        print("Smart home action executed.")

    return wrapper


@log_execution
def adjust_lighting(brightness):
    print(f"Adjusting lighting to {brightness}%.")


adjust_lighting(80)
