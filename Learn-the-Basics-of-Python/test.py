# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, My Name is " + self.name + ".I am " + str(self.age) + " Year Old")



p1 = Person("Stephan", 22)
p1.myfunc()
p1.age = 26
p1.myfunc()


class Stranger:
    def __init__(whatever,name, address):
        whatever.name = name
        whatever.address = address

    def show_name(self):
        print("Hello, My Name is " + self.name + ".I am from " + self.address)

s1 = Stranger("Stephan","Godda")
s1.show_name()

class newClasshere:
    pass

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
