from base import Vehicle
from car import Car
from engine import Engine
from exceptions import NotEnoughFuel, CargoOverload
from plane import Plane

vehicle = Vehicle(weight=1500, fuel=10, fuel_consumption=0.1)

try:
    vehicle.start()
    print("Машина завелась успешно.")
except Exception as e:
    print(str(e))


try:
    vehicle.move(100)
    print(f"Машина прошла ещё 100 км. Осталось топлива: {vehicle.fuel:.2f} л")
except NotEnoughFuel as e:
    print(e)


my_engine = Engine(volume=2.0, pistons=4)
print(my_engine)


my_car = Car(weight=1500, fuel=50, fuel_consumption=0.1)

my_car.set_engine(my_engine)

print(my_car.engine.volume)
print(my_car.engine.pistons)


plane = Plane(weight=10000, fuel=500, fuel_consumption=0.1, cargo=1000, max_cargo=5000)
plane.load_cargo(2000)
print(f"Груз после загрузки: {plane.cargo}")

try:
    plane.load_cargo(3000)
except CargoOverload as e:
    print(e)


previous_cargo = plane.remove_all_cargo()
print(f"Cброc груза: {previous_cargo}")