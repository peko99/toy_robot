from models import Table, Robot


def test_place():
    robot = Robot(Table())
    robot.place(1, 2, "NORTH")
    assert robot.x == 1
    assert robot.y == 2
    assert robot.direction.name == "NORTH"


def test_place_invalid():
    robot = Robot(Table())
    robot.place(6, 6, "SOUTH")
    assert robot.x is None
    assert robot.y is None
    assert robot.direction is None


def test_move():
    robot = Robot(Table())
    robot.place(1, 2, "WEST")
    robot.move()
    assert robot.x == 0
    assert robot.y == 2
    assert robot.direction.name == "WEST"


def test_move_invalid():
    robot = Robot(Table())
    robot.place(4, 4, "EAST")
    robot.move()
    assert robot.x == 4
    assert robot.y == 4
    assert robot.direction.name == "EAST"


def test_left():
    robot = Robot(Table())
    robot.place(1, 1, "NORTH")
    robot.left()
    assert robot.direction.name == "WEST"
    robot.left()
    assert robot.direction.name == "SOUTH"
    robot.left()
    assert robot.direction.name == "EAST"
    robot.left()
    assert robot.direction.name == "NORTH"


def test_right():
    robot = Robot(Table())
    robot.place(1, 1, "NORTH")
    robot.right()
    assert robot.direction.name == "EAST"
    robot.right()
    assert robot.direction.name == "SOUTH"
    robot.right()
    assert robot.direction.name == "WEST"
    robot.right()
    assert robot.direction.name == "NORTH"


def test_report():
    robot = Robot(Table())
    robot.place(2, 2, "EAST")
    report = robot.report()
    assert report == "2,2,EAST"


def test_report_invalid():
    robot = Robot(Table())
    report = robot.report()
    assert report is None


def test_complex():
    robot = Robot(Table())
    robot.place(2, 2, "EAST")
    robot.move()
    robot.move()
    assert robot.x == 4
    assert robot.y == 2
    assert robot.direction.name == "EAST"
    robot.right()
    robot.move()
    robot.move()
    assert robot.x == 4
    assert robot.y == 0
    assert robot.direction.name == "SOUTH"
    robot.move()
    assert robot.x == 4
    assert robot.y == 0
    assert robot.direction.name == "SOUTH"
