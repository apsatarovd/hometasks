#first task
#1.Напишите итератор, который перебирает только четные числа из заданного диапазона.
def range(start, end):
    path = start
    while path < end:
        if path % 2 == 0:
         yield path
        path += 1

for number in range(1, 13):
    print(number)  
        
#second task 
#2. Создайте декоратор, который измеряет время выполнения функции.
import time

def time_of_function(func):
   def wrapper():
      t1 = time.time()
      func()
      t2 = time.time()
      result = t2 - t1 
      print (f"Работа заняла {result} секунд")
      return result
   return wrapper
@time_of_function
def func_one():
   my_list = [x for x in range(1, 100000)]

func_one()
pass

#three task
#3.Создайте декоратор, который проверяет типы аргументов функции и выбрасывает исключение, если типы неверны.
def type_check(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, str)):
                raise TypeError(f"Аргумент {arg} должен быть int или str")
        return func(*args, **kwargs)
    return wrapper

@type_check
def example_function(number, text):
    print(f"Число: {number}, Текст: {text}")

example_function(8, "Notebook")

