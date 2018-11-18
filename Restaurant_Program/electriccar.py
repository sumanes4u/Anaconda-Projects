from car import Car
from battery import Battery

class ElectricCar(Car):
    def __init__(self,manifacturer,model,year):
        super().__init__(manifacturer,model,year)
        self.battery = Battery()


Ritz = ElectricCar('maruthi','ritz',2013)
print(Ritz.battery.battery_size)
print(Ritz.battery.describe_battery())
print(Ritz.battery.upgrade_battery())
print(Ritz.battery.get_range())
print(Ritz.battery.upgrade_battery())
print(Ritz.battery.battery_size)
print(Ritz.battery.upgrade_battery())
