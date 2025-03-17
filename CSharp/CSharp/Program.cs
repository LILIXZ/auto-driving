// See https://aka.ms/new-console-template for more information
using CSharp;

class Program
{
    static void Main()
    {
        SimulationService simulationService;
        var validOptions = new List<int> { 1, 2 };
        int option;
        while (true)
        {
            Field field;

            Console.Write("Welcome to Auto Driving Car Simulation!\n\nPlease enter the width and height of the simulation field in x y format: ");

            // Getting Field info
            while (true)
            {
                try
                {
                    String[] fieldSize = Console.ReadLine().Split();
                    field = new Field(int.Parse(fieldSize[0]), int.Parse(fieldSize[1]));
                    simulationService = new SimulationService(field);
                    break;
                }
                catch (System.Exception)
                {
                    Console.WriteLine("Invalid input. Please enter two integers separated by a space.");
                    Console.Write("Please enter the width and height of the simulation field in x y format: ");
                }
            }

            Console.WriteLine($"You have created a field of {field.Width} x {field.Height}.");

            while (true)
            {
                Console.WriteLine("\nPlease choose from the following options:\n[1] Add a car to field\n[2] Run simulation");

                while (true)
                {
                    Console.Write("Enter your choice: ");
                    try
                    {
                        option = int.Parse(Console.ReadLine());
                        if (!validOptions.Contains(option))
                        {
                            throw new Exception("Invalid choice.");
                        }
                        break;
                    }
                    catch(Exception)
                    {
                        Console.WriteLine("Invalid choice. Please try again.");
                    }
                }

                if (option == 1)
                {
                    simulationService.AddCar();
                }
                else if (option == 2)
                {
                    SimulationService simulation = new SimulationService(field);
                    simulation.RunSimulation();
                    break;
                }
            }

            Console.WriteLine("\nPlease choose from the following options:\n[1] Start over: \n[2] Exit ");
            while (true)
            {
                try{
                    Console.Write("Enter your choice: ");
                    option = int.Parse(Console.ReadLine());
                    if (!validOptions.Contains(option))
                    {
                        throw new Exception("Invalid choice.");
                    }
                    break;
                }catch (Exception)
                {
                    Console.WriteLine("Invalid choice. Please try again.");
                }
            }

            if (option == 2)
            {
                Console.WriteLine("Thank you for running the simulation. Goodbye!");
                break;
            }
        }
    }
}
