from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, cargo=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        total_cargo = self.cargo + add_cargo
        if total_cargo > self.max_cargo:
            raise CargoOverload("Груз превышает максимальную грузоподъемность")
        self.cargo = total_cargo

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo