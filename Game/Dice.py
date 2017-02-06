from random import randrange

def six_sided():
    return randrange(1, 7)

def four_sided():
    return randrange(1, 5)

def eight_sided():
    return randrange(1, 9)

def ten_sided():
    return randrange(1, 11)

def twenty_sided():
    return randrange(1, 21)

def Three_Six_Sided(reject_lowest):
    a = six_sided()
    b = six_sided()
    c = six_sided()

    return a + b + c