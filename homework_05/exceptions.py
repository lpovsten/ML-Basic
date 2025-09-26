class LowFuelError(Exception):
    """Исключение - недостаточно топлива."""
    pass

class NotEnoughFuel(Exception):
    """Исключение - недостаточно топлива для движения."""
    pass

class CargoOverload(Exception):
    """Исключение - груз превышает допустимый вес."""
    pass