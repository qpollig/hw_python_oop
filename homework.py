class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type,
                 duration,
                 distance,
                 speed,
                 calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message = InfoMessage(self.training_type,
                 self.duration,
                 self.get_distance(),
                 self.get_mean_speed(),
                 self.get_spent_calories())
        return message


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    training_type: str = 'Running'
    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_distance(self, LEN_STEP = 0.65) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        time_min_duration = self.duration * 60
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER *
                           self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.weight / self.M_IN_KM * time_min_duration)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    training_type: str = 'Sports Walking'

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        speed_sec = self.get_mean_speed() * 1000 / 3600
        height_meters = self.height / 100
        time_min_duration = self.duration * 60
        spent_calories = ((0.035 * self.weight + (speed_sec ** 2 / height_meters)
 * 0.029 * self.weight) * time_min_duration)
        return spent_calories



class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    training_type: str = 'Swimming'

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return speed

    def get_spent_calories(self) -> float:
        spent_calories = (self.get_mean_speed() + 1.1) * 2 * self.weight * self.duration
        return spent_calories



def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    packages_true = {}
    if workout_type == 'SWM':
        '''training_type = 'Swimming'
        action: int = data[0]
        duration: float = data[1]
        weight: float = data[2]
        length_pool: float = data[3]
        count_pool: float = data[4]
        swim = Swimming(action, duration, weight, length_pool, count_pool, training_type)
        distance = swim.get_distance()
        speed = swim.get_mean_speed()
        calories = swim.get_spent_calories(speed)
        message = swim.show_training_info()
        print(message.get_message())
'''
        packages_true[workout_type] = Swimming.__name__
        swm = Swimming(data[0], data[1], data[2], data[3], data[4])
        return swm
    elif workout_type == 'RUN':
        pass
    elif workout_type == 'WLK':
        pass
    else:
        return False


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
