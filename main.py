from models import Robot, Table


def main():
    width = int(input("Enter the width of the table: "))
    height = int(input("Enter the height of the table: "))
    table = Table(width, height)
    robot = Robot(table)

    command = input("Enter a command: ")


if __name__ == "__main__":
    main()
