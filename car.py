class Car():
    def __init__(self, name, speed, model, color):
        # Initialization
        self.name = name
        self.speed = speed
        self.model = model
        self.color = color
    
    def info(self):
        # Display infos about the car
        print("The car name is {}, with a speed of {} km/h, model {}, in a {} color.".format(self.name, self.speed, self.model, self.color))
    
# Create instances of the Car class(instanciation)
car1 = Car("Ferrari", 420, 2023, "Red")
car2 = Car("Mercedes Benz", 280, 2020, "Black")

# Display infos about each car
car1.info()
car2.info()