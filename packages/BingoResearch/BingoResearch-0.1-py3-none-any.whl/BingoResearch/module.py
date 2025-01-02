def my_function(x):
    return x * x

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    print(my_function(9))
    obj = MyClass("Bob")
    print(obj.greet())
