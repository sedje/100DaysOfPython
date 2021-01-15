import time

current_time = time.time()
print(current_time)

''' sample code from repl.it for using decorators, speed_calc_decorator was completed by me. '''


def speed_calc_decorator(function):
    start_time = time.time()
    function()
    run_time = time.time() - start_time
    print(f"Function {function.__name__} ran for {run_time}s")


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
