from models import Car, Field


def get_user_choice(prompt, valid_choices):
    """
    Prompt the user to make a choice from a list of valid options.
    Args:
        prompt (str): The message displayed to the user to prompt for input.
        valid_choices (list): A list of valid choices that the user can select from.
    Returns:
        str: The user's choice if it is in the list of valid choices.
    """

    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


def start_menu():
    """
    Displays a start menu with options for the user to choose from and returns the user's choice.
    The menu includes the following options:
    [1] Add a car to field
    [2] Run simulation
    Returns:
        str: The user's choice, either "1" or "2".
    """

    print("Please choose from the following options:")
    print("[1] Add a car to field")
    print("[2] Run simulation")
    return get_user_choice("Enter your choice: ", ("1", "2"))


def end_menu():
    """
    Displays an end menu with options for the user to either start over or exit.
    Returns the user's choice as a string.
    Returns:
        str: The user's choice, either "1" for starting over or "2" for exiting.
    """

    print("Please choose from the following options:")
    print("[1] Start over: ")
    print("[2] Exit ")

    return get_user_choice("Enter your choice: ", ("1", "2"))


def get_field_size():
    """
    Prompts the user to input the width and height of the simulation field and returns a Field object.
    The function continuously prompts the user until valid integer inputs are provided.
    If the input is invalid, an error message is displayed and the user is prompted again.
    Returns:
        Field: An instance of the Field class with the specified width and height.
    """

    while True:
        try:
            width, height = map(
                int,
                input(
                    "\nWelcome to Auto Driving Car Simulation!\n\nPlease enter the width and height of the simulation field in x y format: "
                ).split(),
            )
            return Field(width, height)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")


def main():
    """
    Main function to run the auto-driving simulation.
    This function continuously prompts the user to create a field and then
    provides a menu to either add a car to the field or run the simulation.
    The simulation can be ended through the end menu.
    The function operates in an infinite loop until the user chooses to exit.
    """

    while True:
        field = get_field_size()
        print(f"You have created a field of {field.width} x {field.height}.")

        while True:
            choice = start_menu()

            if choice == "1":
                add_car(field)
            else:
                run_simulation(field)
                break

        if end_menu() == "2":
            print("Thank you for running the simulation. Goodbye!")
            break


def print_cars(field: Field):
    """
    Prints the list of cars in the given field.
    Args:
        field (Field): The field object containing the list of cars.
    """

    print("\nYour current list of cars are:")
    [print(f"- {car.initial_info}") for car in field.cars]
    print()


def add_car(field: Field):
    """
    Adds a car to the given field with user-provided details.
    Prompts the user to input the car's name, initial position (x, y, direction),
    and a sequence of commands. Validates the inputs and creates a Car object,
    which is then added to the field. If the input is invalid, the user is prompted
    to re-enter the details.
    Args:
        field (Field): The field to which the car will be added.
    Raises:
        ValueError: If the car's initial position or direction is invalid.
    """

    car_name = input("Please enter the name of the car: ").strip()
    while True:
        car_position = input(
            f"Please enter initial position of car {car_name} in x y Direction format: "
        )
        try:
            car_x, car_y, car_direction = car_position.split()
            car_x = int(car_x)
            car_y = int(car_y)
            if car_direction not in ["N", "S", "E", "W"]:
                raise ValueError("Invalid direction")

            break
        except ValueError:
            print(
                "Invalid input. Please enter the position in x y Direction format (e.g., 1 2 N)."
            )

    input_commands = input(f"Please enter the commands for car {car_name}: ").strip()
    commands = list(input_commands)

    try:
        car = Car(car_name, car_x, car_y, car_direction, commands)
        field.add_car(car)
    except ValueError as e:
        print(e)
        return add_car(field)

    print_cars(field)


def run_simulation(field: Field):
    """
    Runs the simulation for the given field until all cars have executed their commands or a collision occurs.
    Args:
        field (Field): The field object containing cars and their commands.
    """

    step = 0
    while any([car.commands for car in field.cars]):
        step += 1
        for car in [c for c in field.cars if c.commands]:
            car.execute_command(car.commands.pop(0), field)

            collided_car = field.detect_collision(car)
            if collided_car:
                summary_result(
                    field,
                    is_collision=True,
                    step=step,
                    collided_cars=[car, collided_car],
                )
                return

    summary_result(field)


def summary_result(field: Field, is_collision=False, step=0, collided_cars=None):
    """
    Summarizes the result of the simulation.
    If a collision occurred, it prints details of the collision.
    Otherwise, it prints the final positions and directions of all cars.
    Args:
        field (Field): The field object containing the cars.
        is_collision (bool): Indicates if a collision occurred during the simulation.
        step (int): The step number at which the collision occurred.
        collided_cars (list): A list of cars that collided, if any.
    """
    
    print_cars(field)
    print("\nAfter simulation, the result is:")
    if is_collision and collided_cars:
        print(
            f"- {collided_cars[0].name}, collides with {collided_cars[1].name} at ({collided_cars[0].x}, {collided_cars[0].y}) at step {step}."
        )
        print(
            f"- {collided_cars[1].name}, collides with {collided_cars[0].name} at ({collided_cars[1].x}, {collided_cars[1].y}) at step {step}."
        )
    else:
        [
            print(f"- {car.name} ({car.x}, {car.y}) {car.direction}")
            for car in field.cars
        ]
    print()


if __name__ == "__main__":
    main()
