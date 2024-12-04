def log(func):
    
    def run(data):
        print(func(data))
    
    return run