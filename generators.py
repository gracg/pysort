import os.path
from random import randint, shuffle


def ints(minv=0, maxv=100, length=10) -> list[int]:

    if type(minv) != int or type(maxv) != int or type(length) != int:
        raise TypeError("minv,maxv,length can only be integers")

    nums: list[int] = []

    for _ in range(length):
        nums.append(randint(minv, maxv))

    return nums


def words(length, testPath=None):

    if type(length) != int:
        raise TypeError("length param can only be an integer")

    l = []

    if length <= 0:
        return []

    path = 'words.txt'
    # used only in testing
    if testPath is not None:
        if type(testPath) != str:
            raise ValueError("testPath can only be a string")

        path = testPath

    with open(path, 'r') as file:
        lines = file.readlines()
        for w in lines:
            l.append(w.rstrip())

    shuffle(l)

    return l[:length]
