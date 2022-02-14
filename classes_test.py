# This is a sample Python script.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import random


def gen_string(nr: int = 5) -> str:
    # return ''.join(random.choice(string.ascii_lowercase) for i in range(nr))
    return ''.join(random.choices(string.ascii_lowercase, k=nr))


class DummyFTP:
    def __init__(self, name):
        self.name = name

    def dummy_cwd(self):
        print(''.join(self.name for i in range(3)))

class Client:
    # daca e definit aici in toate instantele copil are aceiasi valoare
    copil = DummyFTP(gen_string())

    def __init__(self, name):
        self.name = name
        # daca e definit aici copil este diferit in fiecare instanta
        # self.copil = DummyFTP(gen_string())

    def what_name(self):
        # print(self.copil.name)
        self.copil.dummy_cwd()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    c1 = Client('nume1')
    c2 = Client('nume2')

    print(c1.__dict__)
    c1.what_name()
    print(c2.__dict__)
    c2.what_name()
