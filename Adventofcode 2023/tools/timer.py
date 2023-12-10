from timeit import default_timer

def timer(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] taken: {default_timer() - start:.5f} seconds")
        return result
    return wrapper