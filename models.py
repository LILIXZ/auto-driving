from typing import List, Optional


class Car:
    def __init__(self, name: str, x: int, y: int, direction: str, commands: List[str]):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.initial_info = (
            f"{self.name}, {self.x, self.y} {self.direction}, {"".join(commands)}"
        )
        self.validate_attr()

    def validate_attr(self):
        if not self.name or not self.name.strip():
            raise ValueError("Car name cannot be empty")

        if self.x < 0 or self.y < 0:
            raise ValueError("Car position must be greater than or equal to 0")

        if self.direction not in ["N", "E", "S", "W"]:
            raise ValueError("Invalid direction. Please enter N, E, S, or W")

        if set(self.commands) - set(["L", "R", "F"]):
            raise ValueError("Invalid commands. Please enter only L, R, and F")

    def rotate_left(self):
        directions = ["N", "W", "S", "E"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def rotate_right(self):
        directions = ["N", "E", "S", "W"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1

    def execute_command(self, command: str, field: "Field"):
        if command == "L":
            self.rotate_left()
        elif command == "R":
            self.rotate_right()
        elif command == "F":
            prev_x, prev_y = self.x, self.y
            self.move_forward()

            if not field.is_within_bound(self.x, self.y):
                self.x, self.y = prev_x, prev_y



class Field:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cars = []
        self.validate_attr()

    def validate_attr(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be greater than 0")

    def add_car(self, car: Car):
        if car.name in [c.name for c in self.cars]:
            raise ValueError("Car name already exists")

        if not self.is_within_bound(car.x, car.y):
            raise ValueError("Car position is out of bounds")

        if self.detect_collision(car):
            raise ValueError("Car position is already occupied")

        return self.cars.append(car)

    def is_within_bound(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def detect_collision(self, car: Car) -> Optional[Car]:
        return next(
            (c for c in self.cars if c != car and c.x == car.x and c.y == car.y), None
        )
