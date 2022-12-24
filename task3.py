# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
n = int(input("Введите длину списка "))
my_list = []
for i in range(n):
    f = uniform(0, 10)
    my_list.append(round(f, 2))
print(my_list)
min_fr = max_fr = my_list[0] % 1
for i in range(1, len(my_list)):
        if my_list[i] % 1 < min_fr:
            min_fr = my_list[i] % 1
        elif my_list[i] % 1 > max_fr:
            max_fr = my_list[i] % 1
        else:
            continue
print(round(max_fr - min_fr, 2))
