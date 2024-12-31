# hello.py
class HelloWorld:
    def __init__(self, name: str = "World"):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")
