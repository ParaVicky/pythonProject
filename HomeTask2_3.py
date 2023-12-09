# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# Пример
# n=16
# Вывод
# 1
# 2
# 4
# 8
# 16

N = int(input("Введите число: "))
#PowersOfTwo = []
for i in range(N):
    res = 2**i
    if res <= N:
        print(res)
#       PowersOfTwo.append(res)
#print(PowersOfTwo)
