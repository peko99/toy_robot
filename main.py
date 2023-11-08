from models import Robot, Table


def parse_command(command, robot: Robot):
    command_parts = command.split()
    if command_parts[0] == "PLACE" and len(command_parts) == 2:
        _, params = command_parts
        x, y, direction = params.split(",")
        robot.place(int(x), int(y), direction)
    elif robot.x is not None:
        if command == "MOVE":
            robot.move()
        elif command == "LEFT":
            robot.left()
        elif command == "RIGHT":
            robot.right()
        elif command == "REPORT":
            print(robot.report())
        else:
            print("Invalid command")


def main():
    robot = Robot(Table())

    while True:
        command = input("Enter a command: ")
        parse_command(command.upper(), robot)


if __name__ == "__main__":
    main()
