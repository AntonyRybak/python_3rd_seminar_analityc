# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input("Введите количество элементов "))
my_list = []
for i in range(n):
    my_list.append(random.randint(1, 10))
print(my_list)
count = 0
for i in range(1, n, 2):
    count += my_list[i]
print("Сумма элементов на нечетных позициях =", count)
