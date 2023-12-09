# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

class1 = int(input('Введите количество учеников в классе 1: '))
class2 = int(input('Введите количество учеников в классе 2: '))
class3 = int(input('Введите количество учеников в классе 3: '))
total_desks = 0
for i in (class1, class2, class3):
    total_desks += i//2+(i % 2)
print(total_desks)