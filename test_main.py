import unittest
from main import run_simulation
from models import Car, Field

class TestCarSimulation(unittest.TestCase):
    def setUp(self):
        self.field = Field(5, 5)

    def test_add_car(self):
        car = Car("A", 1, 2, "N", ["L", "F", "R"])
        self.field.add_car(car)
        self.assertEqual(len(self.field.cars), 1)
        self.assertEqual(self.field.cars[0].name, "A")
        self.assertEqual(self.field.cars[0].initial_info, "A, (1, 2) N, LFR")

    def test_car_movement_within_bounds(self):
        car = Car("B", 0, 0, "N", ["F"])
        self.field.add_car(car)
        car.execute_command("F", self.field)
        self.assertEqual((car.x, car.y), (0, 1))

    def test_car_movement_out_of_bounds(self):
        car = Car("C", 0, 4, "N", ["F"])
        self.field.add_car(car)
        car.execute_command("F", self.field)
        self.assertEqual((car.x, car.y), (0, 4))

    def test_run_simulation_no_collision(self):
        self.field.cars = []
        car1 = Car("A", 0, 0, "N", ["F", "F"])
        car2 = Car("B", 1, 1, "E", ["F", "F"])
        self.field.add_car(car1)
        self.field.add_car(car2)
        run_simulation(self.field)
        self.assertEqual((car1.x, car1.y), (0, 2))
        self.assertEqual((car2.x, car2.y), (3, 1))

    def test_run_simulation_with_collision(self):
        self.field.cars = []
        car1 = Car("A", 0, 0, "N", ["F", "F"])
        car2 = Car("B", 0, 1, "S", ["F", "F"])
        self.field.add_car(car1)
        self.field.add_car(car2)
        run_simulation(self.field)
        self.assertEqual((car1.x, car1.y), (0, 1))
        self.assertEqual((car2.x, car2.y), (0, 1))


if __name__ == "__main__":
    unittest.main()
    

