def log(func):
    
    def run(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    
    return run