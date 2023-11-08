M_IN_KM = 1000
CALORIES_MEAN_SPEED_MULTIPLIER = 18
CALORIES_MEAN_SPEED_SHIFT = 1.79
class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type,
                 duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories


    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self, LEN_STEP) -> float:
        """Получить дистанцию в км."""
        distance = self.action * LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self, distance) -> float:
        """Получить среднюю скорость движения."""
        speed = distance / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type =
        duration =
        distance =
        speed =
        calories =
        message = InfoMessage()
        return


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_distance(self, LEN_STEP = 0.65) -> float:
        return super().get_distance()

    def get_mean_speed(self, distance) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self, speed) -> float:
        time_min_duration = self.duration * 60
        spent_calories = ((CALORIES_MEAN_SPEED_MULTIPLIER *
                           speed + CALORIES_MEAN_SPEED_SHIFT)
                          * self.weight / M_IN_KM * time_min_duration)
        return spent_calories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self, LEN_STEP=0.65) -> float:
        return super().get_distance()

    def get_mean_speed(self, distance) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self, speed) -> float:
        speed_sec = speed * 1000 / 3600
        height_meters = self.height / 100
        time_min_duration = self.duration * 60
        spent_calories = ((0.035 * self.weight + (speed_sec **2 / height_meters)
 * 0.029 * self.weight) * time_min_duration)
        return spent_calories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        return super().get_distance(LEN_STEP = 1.38)

    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool / M_IN_KM / self.duration
        return speed

    def get_spent_calories(self, speed) -> float:
        spent_calories = (speed + 1.1) * 2 * self.weight * self.duration
        return spent_calories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type is 'SWM':
        swim = Swimming(data[0], data[1], data[2], data[3], data[4])
        swim.get_distance()
        speed = swim.get_mean_speed()
        swim.get_spent_calories(speed)
        swim.show_training_info()
    elif workout_type is 'RUN':
        pass
    elif workout_type is 'WLK':
        pass
    else:
        return False


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

