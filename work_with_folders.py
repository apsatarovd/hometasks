
#first task 
#1. Напишите программу, которая считывает файл и выводит количество строк, слов и символов в нем.
def count_file_stats(text):
    lines = 0
    words = 0
    chars = 0

    with open(text ,'r') as f:
        for line in f:
            print(line)
            lines += 1
            line_words= line.split()
            words += len(line_words)
            chars += len(line)

    print(f"Количество строк: {lines}")
    print(f"Количество слов: {words}")
    print(f"Количество символов: {chars}")

count_file_stats(text="./text.txt")

#second task
#2. Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только четные числа.
def get_even_numbers(number_list):
    return[number for number in number_list if number % 2 == 0]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_even_numbers(numbers_list)
print(result)



#third task
#3. Используя list comprehension, создайте список всех делителей числа 100. Делитель 100 - это все числа меньше 100 которые делят 100 без остатка.
def get_divisors(number):
    return [i for i in range(1, number) if number % i == 0]

number = 100
result = get_divisors(number)
print(f"Делители числа {number}:{result}")




