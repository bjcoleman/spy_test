import os


def foo():
    bar()
    return 42


def bar():
    os.remove('empty.txt')

