# This is a sample Python script.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import random


def gen_string(nr: int = 5) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(nr))


class DummyFTP:
    def __init__(self, name):
        self.name = name


class Client:
    # copil = DummyFTP(gen_string())

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.copil = DummyFTP(gen_string())

    # @staticmethod
    def what_name(self):
        print(self.copil.name)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    c1 = Client('alin', 'gigica', 'paxx')
    c2 = Client('marius', 'plm', '34255')

    c1.what_name()
    c2.what_name()
