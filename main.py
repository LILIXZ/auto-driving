from models import Car, Field


def get_user_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


def start_menu():
    print("Please choose from the following options:")
    print("[1] Add a car to field")
    print("[2] Run simulation")
    return get_user_choice("Enter your choice: ", ("1", "2"))


def end_menu():
    print("Please choose from the following options:")
    print("[1] Start over: ")
    print("[2] Exit ")

    return get_user_choice("Enter your choice: ", ("1", "2"))


def get_field_size():
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
    print("\nYour current list of cars are:")
    [print(f"- {car.initial_info}") for car in field.cars]
    print()


def add_car(field: Field):
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
