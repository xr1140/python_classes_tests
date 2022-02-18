# This is a sample Python script.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import random


def gen_string(nr: int = 5) -> str:
    # return ''.join(random.choice(string.ascii_lowercase) for i in range(nr))
    return ''.join(random.choices(string.ascii_lowercase, k=nr))


def gen_number(nr: int = 5) -> str:
    # return ''.join(random.choice(string.ascii_lowercase) for i in range(nr))
    return ''.join(random.choices(string.digits, k=nr))


class Parent:
    def __init__(self, name):
        self.name = name

    def dummy_name(self):
        print(' '.join(self.name for i in range(3)))


class Child(Parent):

    def __init__(self, id, name):
        super().__init__(name)
        self.id = id

    def what_id(self):
        # print(self.copil.name)
        super().dummy_name()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p1 = Parent("parent")
    c1 = Child("24234", "child")

    print(p1.__dict__)
    print(c1.__dict__)

    p1.dummy_name()
    c1.what_id()
