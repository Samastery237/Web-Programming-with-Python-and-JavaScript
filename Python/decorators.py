def announe(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper

@announe
def hello():
    print("Hello, World!")

hello() 