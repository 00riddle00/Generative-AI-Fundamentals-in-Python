def log_execution(original_function):
    def wrapper():
        print("Executing smart home action...")
        original_function()
        print("Smart home action executed.")

    return wrapper


@log_execution
def adjust_lighting():
    print("Adjusting lighting.")


adjust_lighting()
