class Human:
    def __init__(self , name = "Human" ):
        self.name = name
class Auto:
    def __init__(self , brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, human):
        self.passengers.append(human)
    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in  self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")
Max = Human("Maxim")
Sviatoslav = Human ("Sviatoslav")
Maxim = Human ("Maxim")
car = Auto("Mercedes")
car.add_passenger(Max)
car.add_passenger(Sviatoslav)
car.add_passenger(Maxim)
car.print_passengers_names()
car1 = Auto("Tesla")
car1.print_passengers_names()
print()