namespace CSharp
{
    public class Field
    {
        public int Width { get; }
        public int Height { get; }
        public List<Car> Cars{ get; }

        public Field(int width, int height)
        {
            Width = width;
            Height = height;
            Cars = new List<Car>(); 
        }

        public void AddCar(Car car){
            Cars.Add(car);
        }
        
        public bool IsWithinBounds(int x, int y)
        {
            return x >= 0 && x < Width && y >= 0 && y < Height;
        }

        public bool IsOccupied(int x, int y)
        {
            return Cars.Any(car => car.X == x && car.Y == y);
        }

        public Car? DetectCollision(Car movingCar)
        {
            return Cars.FirstOrDefault(car => car != movingCar && car.X == movingCar.X && car.Y == movingCar.Y);
        }
    }
}
