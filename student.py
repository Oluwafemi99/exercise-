class car:
    def __init__(self, name, model, type, year):
        self.name = name
        self.model = model
        self.type = type
        self.year = year
        self.odometer = 0

    def car_description(self):
        print(f"This car is {self.name}, {self.model}, year{self.year} {self.type}")

    def odometer_reading(self):
        print(f"the car has {self.odometer} miles")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("you cant roll back the mileage")

    def increament_odometer(self, miles):
        self.odometer += miles


my_car = car("toyota", "corrola", "XE", 2020)
my_car.car_description()
my_car.odometer_reading()
my_car.update_odometer(100)
my_car.odometer_reading()
my_car.increament_odometer(50)
my_car.odometer_reading()
