import random
import time
from datetime import datetime


def time_it(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Execution time: {end - start}")

    return wrapper


@time_it
def simulate_long_task():
    duration = random.randint(1, 3)
    time.sleep(duration)
    print(f"Task completed in {duration} seconds!")


simulate_long_task()
