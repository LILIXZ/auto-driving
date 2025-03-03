from typing import List, Optional


class Car:
    def __init__(self, name: str, x: int, y: int, direction: str, commands: List[str]):
        """
        Initializes a new instance of the class with the given parameters.
        Args:
            name (str): The name of the entity.
            x (int): The x-coordinate of the entity's position.
            y (int): The y-coordinate of the entity's position.
            direction (str): The direction the entity is facing.
            commands (List[str]): A list of commands for the entity to execute.
        """

        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.initial_info = (
            f"{self.name}, {self.x, self.y} {self.direction}, {"".join(commands)}"
        ) #  A formatted string containing the initial information of the entity.
        self.validate_attr()

    def validate_attr(self):
        """
        Validates the attributes of a car object.
        Raises:
            ValueError: If the car name is empty.
            ValueError: If the car position (x or y) is less than 0.
            ValueError: If the car direction is not one of 'N', 'E', 'S', or 'W'.
            ValueError: If the car commands contain invalid characters (only 'L', 'R', and 'F' are allowed).
        """

        if not self.name or not self.name.strip():
            raise ValueError("Car name cannot be empty")

        if self.x < 0 or self.y < 0:
            raise ValueError("Car position must be greater than or equal to 0")

        if self.direction not in ["N", "E", "S", "W"]:
            raise ValueError("Invalid direction. Please enter N, E, S, or W")

        if set(self.commands) - set(["L", "R", "F"]):
            raise ValueError("Invalid commands. Please enter only L, R, and F")

    def rotate_left(self):
        """
        Rotates the car 90 degrees to the left.
        """

        directions = ["N", "W", "S", "E"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def rotate_right(self):
        """
        Rotates the car 90 degrees to the right.
        """

        directions = ["N", "E", "S", "W"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def move_forward(self):
        """
        Moves the car one step forward in the direction it is currently facing.
        """

        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1

    def execute_command(self, command: str, field: "Field"):
        """
        Executes a given command to control the movement of an object within a field.
        Args:
            command (str): The command to execute. Can be "L" (rotate left), "R" (rotate right), or "F" (move forward).
            field (Field): The field within which the object is moving. Used to check boundary constraints.
        """

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
        """
        Initializes the model with the given width and height.
        Args:
            width (int): The width of the model.
            height (int): The height of the model.
        """

        self.width = width
        self.height = height
        self.cars = []
        self.validate_attr()

    def validate_attr(self):
        """
        Validates the attributes of the object.
        Raises:
            ValueError: If either width or height is less than or equal to 0.
        """

        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be greater than 0")

    def add_car(self, car: Car):
        """
        Adds a car to the collection of cars if it meets certain conditions.
        Parameters:
            car (Car): The car object to be added.
        Raises:
            ValueError: If the car name already exists in the collection.
            ValueError: If the car's position is out of bounds.
            ValueError: If the car's position is already occupied.
        """

        if car.name in [c.name for c in self.cars]:
            raise ValueError("Car name already exists")

        if not self.is_within_bound(car.x, car.y):
            raise ValueError("Car position is out of bounds")

        if self.detect_collision(car):
            raise ValueError("Car position is already occupied")

        return self.cars.append(car)

    def is_within_bound(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates (x, y) are within the bounds of the defined width and height.
        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.
        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        
        return 0 <= x < self.width and 0 <= y < self.height

    def detect_collision(self, car: Car) -> Optional[Car]:
        """
        Detects if the given car has collided with any other car in the list of cars.
        Args:
            car (Car): The car to check for collisions.
        Returns:
            Optional[Car]: The car that has collided with the given car, or None if no collision is detected.
        """

        return next(
            (c for c in self.cars if c != car and c.x == car.x and c.y == car.y), None
        )
