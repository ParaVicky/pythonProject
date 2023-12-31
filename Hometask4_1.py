# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
# Пример
# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5

# var1 = '5 4'
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'

var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

# var1 = '3 4'
# var2 = '1 2 3'
# var3 = '1 2 3 4'

# преобразуем строки в списки целых чисел
set1 = list(map(int, var2.split()))
set2 = list(map(int, var3.split()))

# преобразуем списки во множества
a = set(set1)
b = set(set2)

#находим пересечения и сортируем от мин к макс
common_set = a.intersection(b)
result = sorted(list(common_set))
print(*result)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# i = a.intersection(b)
# print(i)
