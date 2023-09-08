### how to import classes from the python file to another python file and call its functions

To import classes from one Python file into another and call their functions, you can follow these steps:

1. Create the Python file with the class you want to import.
2. Import the class in the second Python file where you want to use it.
3. Create an instance of the imported class.
4. Call the functions or methods of the imported class using the instance.
Here's a step-by-step example:

Suppose you have a file named `myclass.py` with the following content:

```commandline
# myclass.py

class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello from {self.name}!")

    def add_numbers(self, x, y):
        return x + y

```