def announcement(function):
    def wrapper():
        print("Before the wrapped function")
        function()
        print("After the wrapped function")
    return wrapper


@announcement
def hello():
    print("Dipu")


hello()
