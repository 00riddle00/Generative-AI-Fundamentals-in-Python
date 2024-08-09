from datetime import datetime


def add_timestamp(original_function):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        original_function(*args, **kwargs)

    return wrapper


def log_custom_message(message):
    def decorator_function(original_function):
        def wrapper(*args, **kwargs):
            print(message)
            original_function(*args, **kwargs)
            print("Smart home action executed.")

        return wrapper

    return decorator_function


@add_timestamp
@log_custom_message("Initiating brightness adjustment.")
def adjust_lighting(brightness):
    print(f"Adjusting lighting to {brightness}%.")


adjust_lighting(80)
