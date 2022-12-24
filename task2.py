# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input("Введите колчество элементов списка "))
my_list = []    
result = []
for i in range(n):
    my_list.append(random.randint(1, 10))
print(my_list)
for i in range(len(my_list)):
    while i < len(my_list) / 2 and n > len(my_list) / 2:
        n -= 1
        el = my_list[i] * my_list[n]
        result.append(el)
        i += 1
print(result)
