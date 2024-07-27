### Упражнение 1: Создание иерархии классов
# #Задание:
#1. . Создайте абстрактный класс Employee с атрибутами name, age, и position, а также абстрактным методом get_info().
#2. Создайте класс Developer, наследующий от Employee, с дополнительным атрибутом programming_language. Реализуйте метод get_info().
#3. Создайте класс Manager, наследующий от Employee, с дополнительным атрибутом team_size. Реализуйте метод get_info().
#4. Создайте несколько экземпляров классов Developer и Manager, и выведите информацию о каждом из них, используя метод get_info().

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, position):
        self._name = name
        self._age = age
        self._position = position

@abstractmethod
def get_info(self):
    pass 

class Developer(Employee):
    def __init__(self, name, age, position, programming_language):
        super().__init__(name, age, position)
        self._programming_language = programming_language
    def programming_language(self):
        return self._programming_language
    def get_info(self):
        return f"{self._name}, {self._age} years old, {self._position}, uses {self._programming_language}"
    
class Manager(Employee):
    def __init__(self, name, age, position, team_size):
        super().__init__(name, age, position)
        self._team_size = team_size

    def get_info(self):
        return f"{self._name}, {self._age} years old, {self._position}, managing a team of {self._team_size} people"
    
dev1 = Developer("Konor", 33, "Junior C++ Engineer", "C++")
dev2 = Developer("Dastin", 25, "Senior Frontend Engineer", "JavaScript")

print(dev1.get_info())
print(dev2.get_info())

mngr1 = Manager("Kirill", 40, "Middle Backend Team Manager", 2)

print('---------------------------------')
print(mngr1.get_info())

### Упражнение 2: Инкапсуляция и методы доступа
#Задание:
#1. Создайте класс Developer с приватным атрибутом _salary.
#2. Добавьте методы для установки (`set_salary()`) и получения (`get_salary()`) значения приватного атрибута _salary.
#3. Создайте несколько экземпляров класса Developer, установите им зарплаты и выведите эти значения, используя методы доступа.

class Developer:
    def __init__(self, name, age, position, salary, programming_language):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary
        self._programming_language = programming_language

    def get_info(self):
        return f"{self._name}, {self._age} years old, {self._position}, uses {self._programming_language}"

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

dev1 = Developer("Konor", 33, "Junior Python Engineer", 0 , "Python")
dev1.set_salary(70000)
dev2 = Developer("Dastin", 25, "Senior Frontend Engineer", 0 , "JavaScript")
dev2.set_salary(100000)

print(dev1.get_info())
print(dev2.get_info())

print(f"{dev1._name}'s salary is: {dev1.get_salary()}")
print(f"{dev2._name}'s salary is: {dev2.get_salary()}")


 ### Упражнение 3: Полиморфизм и обобщение
#Задание:

#1. Создайте классы Developer, Manager и Intern, наследующие от Employee, каждый со своим методом get_info().
#2. Создайте универсальную функцию print_employee_info(), которая принимает объект типа Employee и вызывает его метод get_info().
#3. Создайте несколько объектов различных классов и вызовите функцию print_employee_info() для каждого из них.

class Employee:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    def get_info(self):
        pass

class Developer(Employee):
    def __init__(self, name, position, programming_language):
        super().__init__(name, position)
        self._programming_language = programming_language

    def get_info(self):
        return f"{self._name}, {self._position}, uses {self._programming_language}"

class Manager(Employee):
    def __init__(self, name, position, programming_language, age):
        super().__init__(name, position)
        self._programming_language = programming_language
        self._age = age

    def get_info(self):
        return f"{self._name}, {self._position}, uses {self._programming_language}, {self._age} years old"

class Intern(Employee):
    def __init__(self, name, position, programming_language, age, project):
        super().__init__(name, position)
        self._programming_language = programming_language
        self._age = age
        self._project = project

    def get_info(self):
        return f"{self._name}, {self._position}, uses {self._programming_language}, {self._age} years old, is working on a project {self._project}"

dev = Developer("Jon", "Systems analyst Developer", "C++")
mngr = Manager("Khabib", "Senior Manager", "Python", 35)
intr = Intern("Pudge", "Intern", "Java", 19, "Chatbot")

def print_employee_info(employee):
    print(employee.get_info())

employees = [dev, mngr, intr]
for emp in employees:
    print_employee_info(emp)
