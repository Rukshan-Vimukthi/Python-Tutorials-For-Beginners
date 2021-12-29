"""This python module contains a class named cube"""


class Cube:
    cube_width = 0
    cube_height = 0
    cube_length = 0

    def __init__(self):
        pass

    def change_width(self, width):
        self.cube_width = width

    def get_width(self):
        return self.cube_width


cube_object = Cube()
width = cube_object.get_width()


class ClassWithArguments:
    def __init__(self, argument_1, argument_2):
        print(argument_1, argument_2)

    def second_method(self):
        print("Hello World")


ClassWithArguments("Hello", "User")

