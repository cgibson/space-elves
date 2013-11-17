

class Position (object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Position(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Position(self.x - o.x, self.y - o.y)

    def __mul__(self, scalar):
        return Position(self.x * scalar, self.y * scalar)

    def __mul__(self, scalar):
        return Position(self.x / scalar, self.y / scalar)

    def __getitem__(self, item):

        if item == 0:
            return self.x
        if item == 1:
            return self.y

    def __len__(self):
        return 2