from math import sqrt, pi

class Rocket:
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
      
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
       
        distance = sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)
        return distance
    
    def __str__(self):
        return f"A Rocket positioned at ({self.x},{self.y})"

    def __repr__(self):
        return f"Rocket({self.x},{self.y})"

    def __eq__(self, other):
       
        if isinstance(other, Rocket):
            return self.x == other.x and self.y == other.y
        return False

class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
    def __str__(self):
        return f"Shuttle at ({self.x}, {self.y}) with {self.flights_completed} flights completed"

class CircleRocket(Rocket):
    def __init__(self, x=0, y=0, radius=1):
        
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        
        return pi * (self.radius ** 2)

    def get_circumference(self):
       
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"CircleRocket at ({self.x}, {self.y}) with radius {self.radius}"

if __name__ == "__main__":
    # Testing the Rocket class
    rocket_0 = Rocket(10, 20)
    print(rocket_0)  # A Rocket positioned at (10,20)
    
    # Testing the Shuttle class
    shuttle_0 = Shuttle(5, 15, 3)
    print(shuttle_0)  # Shuttle at (5, 15) with 3 flights completed
    
    # Testing the CircleRocket class
    circle_rocket_0 = CircleRocket(0, 0, 5)
    print(circle_rocket_0)  # CircleRocket at (0, 0) with radius 5
    print("Area:", circle_rocket_0.get_area())  # Area: 78.53981633974483
    print("Circumference:", circle_rocket_0.get_circumference())  # Circumference: 31.41592653589793