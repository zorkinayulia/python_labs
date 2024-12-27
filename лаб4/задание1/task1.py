class Vehicle:
    """
    Базовый класс для представления транспортных средств.
    :param name (str): Название транспортного средства
    :param speed (float): Максимальная скорость транспортного средства (км/ч)
    Примеры:
    >>> vehicle = Vehicle("самолет", 700)
    """

    def __init__(self, name: str, speed: float) -> None:
        """
        Инициализирует транспортное средство с указанным названием и скоростью.
        :param name (str): Название транспортного средства
        :param speed (float): Максимальная скорость
        """
        self.name = name
        self.speed = speed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.
        """
        return f"Транспортное средство: {self.name}, Максимальная скорость: {self.speed} км/ч"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика.
        """
        return f"Vehicle(name={self.name!r}, speed={self.speed!r})"

    def move(self) -> str:
        """
        Функция движения транспортного средства.
        """
        return f"{self.name} движется со скоростью {self.speed} км/ч."


class Car(Vehicle):
    """
    Дочерний класс для представления автомобиля.
    :param name (str): Название автомобиля
    :param speed (float): Максимальная скорость
    :param seats (int): Количество мест в автомобиле
    Пример:
    >>> car = Car('БМВ', 270, 2)
    """

    def __init__(self, name: str, speed: float, seats: int) -> None:
        """
        Инициализирует автомобиль с названием, скоростью и количеством мест.
        :param name (str): Название автомобиля.
        :param speed (float): Максимальная скорость.
        :param seats (int): Количество мест.
        """
        super().__init__(name, speed)
        self.seats = seats

    def __str__(self) -> str:
        """
        Перегруженный метод для представления автомобиля.
        """
        return f"Легковой автомобиль: {self.name}, Скорость: {self.speed} км/ч, Мест: {self.seats}"

    def move(self) -> str:
        """
        Перегруженный метод движения.
        Причина перегрузки:
        У автомобилей движение подразумевает добавление дополнительного описания.
        """
        return f"{self.name} движется по дороге со скоростью {self.speed} км/ч."

    def refuel(self) -> str:
        """
        Функция заправки автомобиля.
        """
        return f"Автомобиль {self.name} заправлен."


if __name__ == "__main__":
    vehicle = Vehicle('Самолёт', 60)
    car = Car('Мерседес', 220, 5)

    print(vehicle)
    print(repr(vehicle))
    print(vehicle.move())

    print(car)
    print(repr(car))
    print(car.move())
    print(car.refuel())