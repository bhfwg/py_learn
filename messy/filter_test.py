li = [0, 1, 'a', '', ' ', None]
lit = filter(None, li)
print li
print lit


def my_filter(item):
    if isinstance(item, str):
        return True
    else:
        return False

print
li = [0, 1, 'a', '', ' ', None]
lit = filter(my_filter, li)
print li
print lit


class Nonsense(object):

    def __init__(self, sense):
        self.sense = sense

    def __repr__(self):
        return repr(self.sense)

li = [
    Nonsense(None),
    Nonsense(0),
    Nonsense([]),
    Nonsense(1),
    Nonsense({}),
    Nonsense('href'),
]
print filter(lambda x: x.sense, li)
