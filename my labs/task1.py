import doctest


class Train:
    def __init__(self, length: float, max_speed: float):
        """
        Создание и подготовка к работе объекта "Поезд"
        :param length: Длина поезда (м)
        :param max_speed: Максимальная скорость поезда (км/ч)
        Примеры:
        >>> train = Train(500, 350)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина поезда должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина поезда должна быть положительным числом")
        self.length = length

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость поезда должна"
                            " быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость поезда должна"
                             " быть положительным числом")
        self.max_speed = max_speed

    def check_train_params(self) -> list:
        """
        Функция которая возращает характеристики поезда
        :return: [длина, макс. скорость]
        Примеры:
        >>> train = Train(500, 350)
        >>> train.check_train_params()
        [500, 350]
        """
        return [self.length, self.max_speed]

    def set_new_train_params(self, length: float, max_speed: float) -> str:
        """
        Функция которая возращает характеристики поезда
        :return: [длина, макс. скорость]
        Примеры:
        >>> train = Train(500, 350)
        >>> train.set_new_train_params(100, 200)
        'Характеристики поезда были успешно обновлены. 100 м. и 200 км/ч'
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина поезда должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина поезда должна быть положительным числом")
        self.length = length

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость поезда должна"
                            " быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость поезда должна"
                             "быть положительным числом")
        self.max_speed = max_speed

        return (f'Характеристики поезда были успешно обновлены. '
                f'{length} м. и {max_speed} км/ч')


class Student:
    def __init__(self, course: int, average_mark: float):
        """
        Создание и подготовка к работе объекта "Студент"
        :param course: Номер курса
        :param average_mark: Средний балл
        Примеры:
        >>> student = Student(2, 4.5)  # инициализация экземпляра класса
        """
        if not isinstance(course, int):
            raise TypeError("Номер курса должен быть типа int")
        if not (1 <= course <= 5):
            raise ValueError("Номер курса должен быть от 1 до 5")
        self.course = course

        if not isinstance(average_mark, (int, float)):
            raise TypeError("Средний балл должен быть типа int или float")
        if not (2 <= average_mark <= 5):
            raise ValueError("Средний балл должен быть от 2 до 5")
        self.average_mark = average_mark

    def check_average_mark(self) -> float:
        """
        Функция которая возращает средний балл студента
        :return: Средний балл
        >>> student = Student(2, 4.5)
        >>> student.check_average_mark()
        4.5
        """
        return self.average_mark

    def check_course(self) -> int:
        """
        Функция которая возращает номер курса студента
        :return: Курс
        >>> student = Student(2, 4.5)
        >>> student.check_course()
        2
        """
        return self.course

    def set_new_student_params(self, course: int, average_mark: float) -> str:
        """
        Функция которая устанавливает новые значения курса и среднего балла
        :return: [курс, средний балл]
        Примеры:
        >>> student = Student(2, 4.5)
        >>> student.set_new_student_params(1, 5.0)
        'Значения были успешно обновлены. 1 и 5.0'
        """
        if not isinstance(course, int):
            raise TypeError("Номер курса должен быть типа int")
        if not (1 <= course <= 5):
            raise ValueError("Номер курса должен быть от 1 до 5")
        self.course = course

        if not isinstance(average_mark, (int, float)):
            raise TypeError("Средний балл должен быть типа int или float")
        if not (2 <= average_mark <= 5):
            raise ValueError("Средний балл должен быть от 2 до 5")
        self.average_mark = average_mark

        return f'Значения были успешно обновлены. {course} и {average_mark}'


class Car:
    def __init__(self, avg_speed: float, volume_of_gas: float,
                 avg_gas_consumption: float, max_volume=60):
        """
        Создание и подготовка к работе объекта "Машина"
        :param avg_speed: Средняя скорость (км/ч)
        :param volume_of_gas: Объем бензина (л)
        :param avg_gas_consumption: Средний расход бензина (л/100 км)
        :param max_volume: Максимальный объем бака (по умолчанию: 60 литров)
        Примеры:
        >>> car = Car(55, 40, 12)  # инициализация экземпляра класса
        """
        if not isinstance(avg_speed, (int, float)):
            raise TypeError("Средняя скорость должна быть типа int или float")
        if avg_speed <= 0:
            raise ValueError("Средняя скорость должна"
                             " быть положительным числом")
        self.avg_speed = avg_speed

        if not isinstance(volume_of_gas, (int, float)):
            raise TypeError("Объем бензина должен быть типа int или float")
        if not (0 <= volume_of_gas <= max_volume):
            raise ValueError("Объем бензина должен быть положительным числом"
                             " и не больше максимального объема бака")
        self.volume_of_gas = volume_of_gas

        if not isinstance(avg_gas_consumption, (int, float)):
            raise TypeError("Средний расход бензина должен"
                            " быть типа int или float")
        if avg_gas_consumption <= 0:
            raise ValueError("Средний расход бензина должен"
                             " быть положительным числом")
        self.avg_gas_consumption = avg_gas_consumption

        if not isinstance(max_volume, (int, float)):
            raise TypeError("Объем бензина должен быть типа int или float")
        if not (volume_of_gas <= max_volume):
            raise ValueError("Максимальный объем бака не должен быть"
                             " меньше текущего объема бензина")
        self.max_volume = max_volume

    def refuel_car(self) -> None:
        """
        Функция которая заправляет машину
        :return: Заправлена ли машина
        >>> car = Car(33, 40, 12)
        >>> car.refuel_car()
        """
        self.volume_of_gas = self.max_volume

    def check_how_many_kms_remains(self) -> float:
        """
        Функция которая считает остаток пути,
         исходя из среднего расхода бензина
        :return: Количество км
        >>> car = Car(55, 42, 12)
        >>> car.check_how_many_kms_remains()
        350.0
        """
        result = (self.volume_of_gas / self.avg_gas_consumption) * 100
        return result

    def set_new_car_params(self, avg_speed: float, volume_of_gas: float,
                           avg_gas_consumption: float,
                           max_volume: float) -> str:
        """
        Функция которая считает остаток пути,
         исходя из среднего расхода бензина
        :return: Количество км
        >>> car = Car(55, 42, 12, 60)
        >>> car.set_new_car_params(78, 60, 20, 60)
        'Значения были успешно обновлены. 78 км/ч, 60 л, 20 л/100 км, 60 л.'
        """
        if not isinstance(avg_speed, (int, float)):
            raise TypeError("Средняя скорость должна быть типа int или float")
        if avg_speed <= 0:
            raise ValueError("Средняя скорость должна быть"
                             " положительным числом")
        self.avg_speed = avg_speed

        if not isinstance(volume_of_gas, (int, float)):
            raise TypeError("Объем бензина должен быть типа int или float")
        if not (0 <= volume_of_gas <= max_volume):
            raise ValueError("Объем бензина должен быть положительным числом"
                             " и не больше максимального объема бака")
        self.volume_of_gas = volume_of_gas

        if not isinstance(avg_gas_consumption, (int, float)):
            raise TypeError("Средний расход бензина должен"
                            " быть типа int или float")
        if avg_gas_consumption <= 0:
            raise ValueError("Средний расход бензина должен"
                             " быть положительным числом")
        self.avg_gas_consumption = avg_gas_consumption

        if not isinstance(max_volume, (int, float)):
            raise TypeError("Объем бензина должен быть типа int или float")
        if not (volume_of_gas <= max_volume):
            raise ValueError("Максимальный объем бака не должен быть"
                             " меньше текущего объема бензина")
        self.max_volume = max_volume

        return (f'Значения были успешно обновлены.'
                f' {avg_speed} км/ч, {volume_of_gas} л,'
                f' {avg_gas_consumption} л/100 км, {max_volume} л.')


if __name__ == '__main__':
    doctest.testmod()