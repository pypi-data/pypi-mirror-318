import os

FILE = 'file://'


class Trying:

    BASE = os.path.dirname(os.path.abspath(__file__))


class Htmls:

    BASE = os.path.join(Trying.BASE, 'htmls')
    FRUITS = FILE + os.path.join(BASE, 'fruits.html')
