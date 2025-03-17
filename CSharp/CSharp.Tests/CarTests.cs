using Xunit;
using CSharp;

namespace CSharp.Tests;

public class CarTests
{
    [Fact]
    public void Car_Should_Initialize_With_Correct_Position_And_Direction()
    {
        // Arrange & Act
        Car car = new Car("Tesla", 1, 2, 'N');

        // Assert
        Assert.Equal("Tesla", car.Name);
        Assert.Equal(1, car.X);
        Assert.Equal(2, car.Y);
        Assert.Equal('N', car.Direction);
    }


    [Fact]
    public void Car_Should_Set_Commands()
    {
        // Arrange & Act
        Car car = new Car("Tesla", 1, 2, 'N');
        car.SetCommands("LRFFRL");
        Queue<char> expected = new Queue<char>(['L', 'R', 'F', 'F', 'R', 'L']);

        // Assert
        Assert.Equal(expected, car.Commands);
    }

    [Fact]
    public void Car_Should_Move_Forward()
    {
        // Arrange
        Field field = new Field(5, 5);
        Car car = new Car("Tesla", 1, 2, 'N');
        car.SetCommands("F");

        // Act
        car.ExecuteCommand();

        // Assert
        Assert.Equal(1, car.X);
        Assert.Equal(3, car.Y);  // Moving North
    }

    [Fact]
    public void Car_Should_Turn_Left(){
        // Arrange
        Field field = new Field(5, 5);
        Car car = new Car("Tesla", 1, 2, 'N');
        car.SetCommands("L");

        // Act
        car.ExecuteCommand();

        // Assert
        Assert.Equal('W', car.Direction);
    }

    [Fact]
    public void Car_Should_Turn_Right(){
        // Arrange
        Field field = new Field(5, 5);
        Car car = new Car("Tesla", 1, 2, 'N');
        car.SetCommands("R");

        // Act
        car.ExecuteCommand();

        // Assert
        Assert.Equal('E', car.Direction);
    }
}
