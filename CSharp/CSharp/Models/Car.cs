namespace CSharp
{
    public class Car
    {
        private static readonly HashSet<char> ValidCommands = new() { 'L', 'R', 'F' };
        public string Name { get; }
        public int X { get; set; }
        public int Y { get; set; }
        public char Direction { get; private set; }  // 'N', 'S', 'E', 'W'
        public Queue<char> Commands;
        public String InitialInfo;

        public Car(string name, int x, int y, char direction)
        {
            Name = name;
            X = x;
            Y = y;
            Direction = direction;
            Commands = new Queue<char>("");
            InitialInfo = $"{Name}, ({X}, {Y}), {Direction}, ";
        }

        public void SetCommands(string commandSequence){
            if (!commandSequence.All(c => ValidCommands.Contains(c))){
                throw new ArgumentException("Invalid command found. Only 'L', 'R' and 'F' are allowed.");
            }
            Commands = new Queue<char>(commandSequence);
            InitialInfo += commandSequence;
        }

        public void ExecuteCommand()
        {
            if (Commands.Count == 0) return;

            char command = Commands.Dequeue();
            if (command == 'F')
            {
                MoveForward();
            }
            else if (command == 'L')
            {
                TurnLeft();
            }
            else if (command == 'R')
            {
                TurnRight();
            }
        }
    
        private void MoveForward()
        {
            switch (Direction)
            {
                case 'N': Y++; break;
                case 'S': Y--; break;
                case 'E': X++; break;
                case 'W': X--; break;
            }
        }
    
        private void TurnLeft()
        {
            Direction = Direction switch
            {
                'N' => 'W',
                'W' => 'S',
                'S' => 'E',
                'E' => 'N',
                _ => Direction
            };
        }
    
        private void TurnRight()
        {
            Direction = Direction switch
            {
                'N' => 'E',
                'E' => 'S',
                'S' => 'W',
                'W' => 'N',
                _ => Direction
            };
        }
    }
}
