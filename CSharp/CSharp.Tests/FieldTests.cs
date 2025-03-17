using Xunit;
using CSharp;

namespace CSharp.Tests;

public class FieldTests
{
    [Fact]
    public void Field_Should_Have_Width_And_Height()
    {
        // Arrange & Act
        Field field = new Field(5, 5);

        // Assert
        Assert.Equal(5, field.Width);
        Assert.Equal(5, field.Height);
    }

    [Fact]
    public void Field_Should_Add_Car(){
        // Arrange
        Field field = new Field(5, 5);
        Car car = new Car("Tesla", 1, 2, 'N');

        // Act
        field.AddCar(car);

        // Assert
        Assert.Contains(car, field.Cars);
        Assert.Single(field.Cars);
    }

    [Fact]
    public void Field_Should_Check_Within_Bound()
    {
        // Arrange
        Field field = new Field(5, 5);
        int validX = 4;
        int invalidX = 5;
        
        // Assert
        Assert.True(field.IsWithinBounds(validX, 0));
        Assert.False(field.IsWithinBounds(invalidX, 0));
    }
    
    [Fact]
    public void Field_Should_Detect_Occupied_Postion()
    {
        // Arrange
        Field field = new Field(5, 5);
        Car car = new Car("Tesla", 1, 2, 'N');
        field.AddCar(car);
        
        // Assert
        Assert.True(field.IsOccupied(1, 2));
        Assert.False(field.IsOccupied(2, 1));
    }

    [Fact]
    public void Field_Should_Detect_Collision()
    {
        // Arrange
        Field field = new Field(5, 5);
        Car car = new Car("Tesla", 1, 2, 'N');
        field.AddCar(car);
        Car movingCar = new Car("BMW", 1, 2, 'W');
        
        // Assert
        Assert.Equal(car, field.DetectCollision(movingCar));
    }
}
