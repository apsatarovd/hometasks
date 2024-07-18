#first task
# Создание класса
#1. Создайте класс Car, который будет иметь следующие атрибуты:

#- make (марка)
#- model (модель)
#- year (год выпуска)
#- odometer_reading (пробег)

#2. Создайте методы:
#- init для инициализации атрибутов
#- get_descriptive_name для получения описательного имени автомобиля (например, "2016 Tesla Model S")
#- read_odometer для вывода пробега
#- update_odometer для обновления пробега (с проверкой, что новое значение больше текущего)
# increment_odometer для увеличения пробега на заданное значение

class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        return f"{self.make} {self.model} {self.year}"
    
    def read_odometer(self):
        print(f"Изначальный пробег автомобиля: {self.odometer_reading} километров")
    
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
            print("Ваш пробег обновлен:", self.odometer_reading)
        else:
            print("Пробег не может быть меньше текущего")

my_car = Car(make="Lexus", model="Model ES 250", year=2011)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.update_odometer(7580)

#second task 
# Наследование
#1. Создайте класс ElectricCar, который наследует от класса Car. 

#Добавьте к нему атрибуты:
#- battery_size (емкость батареи, в кВтч)
#- battery_range (запас хода на одной зарядке)

#2. Добавьте методы:
#- describe_battery для вывода информации о батарее
#- get_range для вывода запаса хода
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
class ElectricCar(Car):
    def __init__(self, make, model, battery_size, battery_range):
        super().__init__(make, model)
        self.battery_size = battery_size
        self.battery_range = battery_range
    
    def get_name(self):
        return f"{self.make} {self.model}"
    
    def describe_battery(self):
        return f"Емкость батареи: {self.battery_size} кВтч"
    
    def get_range(self):
        return f"Запас хода на одной зарядке: {self.battery_range} км"

my_electric_car = ElectricCar(make = "Toyota", model = "Prius", battery_size = 67, battery_range = 250)
print(my_electric_car.get_name())
print(my_electric_car.describe_battery())
print(my_electric_car.get_range())

#three task
# Полиморфизм
#1. Создайте класс HybridCar, который наследует от Car и ElectricCar
#  Добавьте к нему атрибут: fuel_tank_size (емкость бензобака)
#2. Добавьте методы:
#- describe_fuel_tank для вывода информации о бензобаке

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
class ElectricCar(Car):
    def __init__(self, make, model, battery_size, battery_range):
        super().__init__(make, model)
        self.battery_size = battery_size
        self.battery_range = battery_range
    
    def get_name(self):
        return f"{self.make} {self.model}"
    
    def describe_battery(self):
        return f"Емкость батареи: {self.battery_size} кВтч"
    
    def get_range(self):
        return f"Запас хода на одной зарядке: {self.battery_range} км"
    

class HybridCar(ElectricCar):
    def __init__(self, make, model, battery_size, battery_range, fuel_tank_size):
        super().__init__(make, model, battery_size, battery_range)
        self.fuel_tank_size = fuel_tank_size
   
    def describe_tank_size(self):
        return f"Емкость бензобака: {self.fuel_tank_size} литров"
    
my_HybridCar = HybridCar(make="Hyundai", model="Sonata Hybrid", battery_size=80, battery_range=380, fuel_tank_size=40)
print(my_HybridCar.get_name())
print(my_HybridCar.describe_battery())
print(my_HybridCar.get_range())
print(my_HybridCar.describe_tank_size())

#fourth task
# Инкапсуляция
#1. Модифицируйте класс Car, добавив приватный атрибут __vin (VIN-номер автомобиля) и метод для его получения (без возможности изменения извне класса).
class Car:
    def __init__(self, make, model, year, vin):
        self.make = make
        self.model = model
        self.year = year
        self._vin = vin  
    def get_name(self):
        return f"{self.make} {self.model} {self.year}"
    
    def get_vin(self):
        return f"Приветный номер автомобиля {self._vin}" 

my_car = Car("Toyota", "Camry", 2022, "AP26062005D")
print(my_car.get_name())
print(my_car.get_vin())  

#fifth task
#  Практическое применение
#1. Создайте объекты различных классов (Car, ElectricCar, HybridCar) и продемонстрируйте использование всех методов.
#2. Вызовите все методы для каждого объекта, чтобы проверить их работу.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} завелась.")

    def stop(self):
        print(f"{self.make} {self.model} заглушили.")

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.make} {self.model} заряжается. Емкость батареи: {self.battery_size} кВтч.")

class HybridCar(Car):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def refuel(self):
        print(f"{self.make} {self.model} заправляется. Тип топлива: {self.fuel_type}.")

my_car = Car("Toyota", "Camry")
my_electric_car = ElectricCar("Tesla", "Model S", 35)
my_hybrid_car = HybridCar("Toyota", "Prius", "бензин")

my_car.start()
my_car.stop()

my_electric_car.charge()

my_hybrid_car.refuel()