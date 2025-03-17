namespace CSharp
{
    public class SimulationService
    {
        public readonly Field SimulationField;
        public SimulationService(Field field)
        {
            SimulationField = field;
        }

        public void RunSimulation()
        {
            int step = 0;
            while (SimulationField.Cars.Any(car => car.Commands.Count > 0))
            {
                step += 1;

                foreach(var car in SimulationField.Cars.Where(car => car.Commands.Count > 0))
                {
                    int prevX = car.X;
                    int prevY = car.Y;

                    car.ExecuteCommand();

                    if (!SimulationField.IsWithinBounds(car.X, car.Y))
                    {
                        car.X = prevX;
                        car.Y = prevY;
                        continue;
                    }

                    var collidedCar = SimulationField.DetectCollision(car);
                    if (collidedCar != null)
                    {
                        DisplayFinalResults(
                            true, step, [car, collidedCar]
                        );
                        return;
                    }
                }
            }

            DisplayFinalResults(false, step, []);
        }


        public void AddCar()
        {
            var validDirections = new char[] { 'N', 'S', 'E', 'W'};

            Console.Write("Please enter the name of the car: ");
            String carName = Console.ReadLine() ?? string.Empty;
            
            Car car;
            while (true) {
                Console.Write($"Please enter initial position of car {carName} in x y Direction format: ");
                try{
                    String[] carPositions = Console.ReadLine().Split();
                    int carX = int.Parse(carPositions[0]);
                    int carY = int.Parse(carPositions[1]);
                    char carDirection = char.Parse(carPositions[2]);

                    if (!validDirections.Contains(carDirection))
                    {
                        throw new Exception("Invalid directions.");
                    }
                    else if (SimulationField.IsOccupied(carX, carY))
                    {
                        throw new Exception("The position is occupied.");
                    }
                    else if (!SimulationField.IsWithinBounds(carX, carY))
                    {
                        throw new Exception("The position is out of bound.");
                    }
                    car = new Car(carName, carX, carY, carDirection);
                    SimulationField.AddCar(car);
                    break;
                }
                catch (Exception)
                {
                    Console.WriteLine("Please re-enter the car position.");
                }
            }

            while (true) {
                Console.Write($"Please enter the commands for car {carName}: ");
                try
                {
                    String commands = Console.ReadLine();
                    car.SetCommands(commands);
                    break;
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                    Console.WriteLine("Please re-enter the movement commands (L, R, F).");
                }
            }
        
            PrintCars();
        }

        public void PrintCars(){
            Console.WriteLine("\nYour current list of cars are:");
            foreach (var car in SimulationField.Cars)
            {
                Console.WriteLine($"- {car.InitialInfo}");
            }
        }


        public void DisplayFinalResults(bool isCollided, int step, Car[] collidedCars)
        {
            PrintCars();
            Console.WriteLine("\nAfter simulation, the result is:");
            if (isCollided && collidedCars.Count() > 0)
            {
                Console.WriteLine(
                    $"- {collidedCars[0].Name}, collides with {collidedCars[1].Name} at ({collidedCars[0].X}, {collidedCars[0].Y}) at step {step}."
                );
                Console.WriteLine(
                    $"- {collidedCars[1].Name}, collides with {collidedCars[0].Name} at ({collidedCars[1].X}, {collidedCars[1].Y}) at step {step}."
                );
            }
            else{
                foreach (Car car in SimulationField.Cars)
                {
                    Console.WriteLine($"- {car.Name} ({car.X}, {car.Y}) {car.Direction}");
                }
            }
        }
    }
}