from exceptions import LowFuelError

class Vehicle:
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):

        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError("Недостаточно топлива для старта двигателя.")
            self.started = True

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel < required_fuel:
            raise NotEnoughFuel("Недостаточно топлива для преодоления переданной дистанции.")
        self.fuel -= required_fuel