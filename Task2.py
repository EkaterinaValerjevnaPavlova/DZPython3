# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

n = int(input('Введите количество элементов в массиве: '))
import random
 
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,10))
print(rand_list)
x = int(input('Введите число х: '))

close_value = rand_list[0]
for i in rand_list:
    if abs(i-x) < abs(close_value-x):
        close_value=i
print(close_value)



