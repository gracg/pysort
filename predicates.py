def intAsc(x, y) -> bool:
    if type(x) != int or type(y) != int:
        raise TypeError()
    return x > y


def intDes(x, y) -> bool:
    if type(x) != int or type(y) != int:
        raise TypeError()

    return x < y


def strAsc(x, y):
    if type(x) != str or type(y) != str:
        raise TypeError()

    return x > y


def strDes(x, y):
    if type(x) != str or type(y) != str:
        raise TypeError()

    return x < y
