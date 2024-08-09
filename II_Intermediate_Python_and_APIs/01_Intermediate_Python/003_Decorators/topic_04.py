def log_execution(original_function):
    def wrapper():
        print("Executing smart home action...")
        original_function()
        print("Smart home action executed.")

    return wrapper


def adjust_lighting():
    print("Adjusting lighting.")


decorated_adjust_lighting = log_execution(adjust_lighting)
decorated_adjust_lighting()
