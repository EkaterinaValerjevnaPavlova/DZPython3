# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1

n = int(input('Введите количество элементов в массиве: '))
import random
 
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,10))
print(rand_list)
x = int(input('Введите число х: '))

count = 0
for i in range(len(rand_list)):
    if rand_list[i] == x:
        count+=1
print(count)

