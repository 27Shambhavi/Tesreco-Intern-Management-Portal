import time
from functools import wraps


def log_execution(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(f"Function Name : {func.__name__}")
        print(f"Execution Time : {execution_time:.6f} seconds")
        print(f"Result : {result}")

        return result

    return wrapper


@log_execution
def calculate_performance(attendance, project_score):

    performance = (attendance * 0.4) + (project_score * 0.6)

    return performance


if __name__ == "__main__":

    calculate_performance(90, 95)