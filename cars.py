import logging
from abc import ABC, abstractmethod

# Настройка отладочного логирования
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AutoDebug')

class Debuggable:
    """Базовый отладочный класс"""
    def debug_log(self, message: str):
        logger.debug(f"[{self.__class__.__name__}] {message}")

class Automobile(ABC, Debuggable):
    def __init__(self, brand: str, model: str):
        super().__init__()
        self._brand = brand
        self._model = model
        self._is_running = False
        self.debug_log(f"Создан {brand} {model}")

    # Свойства
    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def is_running(self) -> bool:
        return self._is_running

    # Методы
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            self.debug_log("Двигатель запущен")
        else:
            self.debug_log("Двигатель уже работает")

    def stop_engine(self):
        if self._is_running:
            self._is_running = False
            self.debug_log("Двигатель остановлен")
        else:
            self.debug_log("Двигатель уже остановлен")

    def drive(self):
        if self._is_running:
            self.debug_log("Едем")
        else:
            self.debug_log("Сначала запустите двигатель")

    def honk(self):
        self.debug_log("Сигналим!")

    def get_info(self):
        return f"{self._brand} {self._model}"

    @abstractmethod
    def get_type(self):
        pass

class Truck(Automobile):
    def __init__(self, brand: str, model: str, max_load: int):
        super().__init__(brand, model)
        self._max_load = max_load
        self._current_load = 0

    # Специфичные свойства
    @property
    def max_load(self):
        return self._max_load

    @property
    def current_load(self):
        return self._current_load

    # Переопределенные методы
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            self.debug_log("Дизельный двигатель грузовика запущен")

    def drive(self):
        if self._is_running:
            self.debug_log("Грузовик медленно едет")
        else:
            self.debug_log("Запустите двигатель")

    def honk(self):
        self.debug_log("ГРОМКИЙ сигнал грузовика!")

    # Специфичные методы
    def load_cargo(self, weight: int):
        if self._current_load + weight <= self._max_load:
            self._current_load += weight
            self.debug_log(f"Загружено {weight} кг")
        else:
            self.debug_log("Перегруз!")

    def unload(self):
        self.debug_log(f"Разгружено {self._current_load} кг")
        self._current_load = 0

    def get_type(self):
        return "Грузовик"

class Car(Automobile):
    def __init__(self, brand: str, model: str, doors: int):
        super().__init__(brand, model)
        self._doors = doors
        self._passengers = 0

    # Специфичные свойства
    @property
    def doors(self):
        return self._doors

    @property
    def passengers(self):
        return self._passengers

    # Переопределенные методы
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            self.debug_log("Двигатель автомобиля запущен")

    def drive(self):
        if self._is_running:
            self.debug_log("Автомобиль быстро едет")
        else:
            self.debug_log("Запустите двигатель")

    def honk(self):
        self.debug_log("Сигнал автомобиля")

    # Специфичные методы
    def add_passenger(self):
        if self._passengers < 4:
            self._passengers += 1
            self.debug_log("Пассажир добавлен")
        else:
            self.debug_log("Нет мест")

    def remove_passenger(self):
        if self._passengers > 0:
            self._passengers -= 1
            self.debug_log("Пассажир вышел")

    def get_type(self):
        return "Легковой автомобиль"

class Bus(Automobile):
    def __init__(self, brand: str, model: str, capacity: int):
        super().__init__(brand, model)
        self._capacity = capacity
        self._passengers = 0

    # Специфичные свойства
    @property
    def capacity(self):
        return self._capacity

    @property
    def passengers(self):
        return self._passengers

    # Переопределенные методы
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            self.debug_log("Двигатель автобуса запущен")

    def drive(self):
        if self._is_running:
            self.debug_log("Автобус едет по маршруту")
        else:
            self.debug_log("Запустите двигатель")

    def honk(self):
        self.debug_log("Сигнал автобуса")

    # Специфичные методы
    def board_passenger(self):
        if self._passengers < self._capacity:
            self._passengers += 1
            self.debug_log("Пассажир вошел")
        else:
            self.debug_log("Автобус полон")

    def exit_passenger(self):
        if self._passengers > 0:
            self._passengers -= 1
            self.debug_log("Пассажир вышел")

    def get_type(self):
        return "Автобус"

# Демонстрация работы
def demo():
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССОВ ===\n")
    
    # Создание объектов
    truck = Truck("Volvo", "FH16", 20000)
    car = Car("Toyota", "Camry", 4)
    bus = Bus("Mercedes", "Sprinter", 20)
    
    vehicles = [truck, car, bus]
    
    # Демонстрация методов
    for vehicle in vehicles:
        print(f"\n--- Работа с {vehicle.get_type()} ---")
        print(vehicle.get_info())
        
        vehicle.start_engine()
        vehicle.drive()
        vehicle.honk()
        vehicle.stop_engine()
        
        # Специфичные методы
        if isinstance(vehicle, Truck):
            vehicle.load_cargo(5000)
            vehicle.unload()
        elif isinstance(vehicle, Car):
            vehicle.add_passenger()
            vehicle.remove_passenger()
        elif isinstance(vehicle, Bus):
            vehicle.board_passenger()
            vehicle.exit_passenger()

if __name__ == "__main__":
    demo()