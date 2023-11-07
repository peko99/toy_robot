from enums import Direction
from models import Table


class Robot:
    def __init__(self, table: Table):
        self.x = None
        self.y = None
        self.direction = None
        self.table = table

    def place(self, x, y, direction):
        if self.table.is_valid_position(x, y) and direction in Direction.__members__:
            self.x = x
            self.y = y
            self.direction = Direction[direction]

    def move(self):
        new_x, new_y = self.calculate_new_position()
        if self.table.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def calculate_new_position(self):
        if self.direction == Direction.NORTH:
            return self.x, self.y + 1
        elif self.direction == Direction.SOUTH:
            return self.x, self.y - 1
        elif self.direction == Direction.EAST:
            return self.x + 1, self.y
        elif self.direction == Direction.WEST:
            return self.x - 1, self.y

    def left(self):
        self.direction = Direction((self.direction.value - 1) % 4)

    def right(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def report(self):
        return f"{self.x},{self.y},{self.direction.name}"
