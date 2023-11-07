class Robot:
    def __init__(self, table):
        self.x = None
        self.y = None
        self.direction = None
        self.table = table

    def place(self, x, y, direction):
        if self.table.is_valid_position(x, y) and direction in [
            "NORTH",
            "WEST",
            "SOUTH",
            "EAST",
        ]:
            self.x = x
            self.y = y
            self.direction = direction

    def move(self):
        if self.direction == "NORTH" and self.table.is_valid_position(
            self.x, self.y + 1
        ):
            self.y += 1
        elif self.direction == "SOUTH" and self.table.is_valid_position(
            self.x, self.y - 1
        ):
            self.y -= 1
        elif self.direction == "EAST" and self.table.is_valid_position(
            self.x + 1, self.y
        ):
            self.x += 1
        elif self.direction == "WEST" and self.table.is_valid_position(
            self.x - 1, self.y
        ):
            self.x -= 1

    def left(self):
        if self.facing == "NORTH":
            self.facing = "WEST"
        elif self.facing == "WEST":
            self.facing = "SOUTH"
        elif self.facing == "SOUTH":
            self.facing = "EAST"
        elif self.facing == "EAST":
            self.facing = "NORTH"

    def right(self):
        if self.facing == "NORTH":
            self.facing = "EAST"
        elif self.facing == "EAST":
            self.facing = "SOUTH"
        elif self.facing == "SOUTH":
            self.facing = "WEST"
        elif self.facing == "WEST":
            self.facing = "NORTH"

    def report(self):
        return f"{self.x},{self.y},{self.direction}"
