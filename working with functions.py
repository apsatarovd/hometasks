# first task
#1. Напишите функцию, которая принимает список чисел и возвращает их сумму.
def sum_of_list(numbers):
    sum = 0 
    for x in numbers:
        sum += x
    return x
numbers = [2,5,11,15]
result  = sum_of_list(numbers)
print(f"Сумма чисел в списке:{result}")


print("-----------------------------------------------------------")

#second task
# Создайте класс Rectangle, который принимает длину и ширину, и включает метод для вычисления площади.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def  square(self):
        return self.length * self.width

a = Rectangle(15 , 30)
a.square()
print (f"Площадь прямоугольника: {a.square()}")


print("-----------------------------------------------------------")


#third task
#3. Создайте модуль с функцией, которая принимает строку и возвращает количество слов в этой строке. Импортируйте и используйте этот модуль в главной программе.

def count_words_in_string(input_string):
    words = input_string.split()
    return len(words)
user_input = input("Введите строку: ")
word_count = count_words_in_string(user_input)
print(f"Количество слов в строке: {word_count}")


 
#fourth task
#4. Написать функцию которая принимает два значения и арифметический оператор, который работает как калькулятор. 
from mymodule import calculator
a = int(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /) ")
b = int(input("Введите второе число: "))

result = calculator(a, operator, b)
print(f"Результат: {result}")

