# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string_part = "a a a b c a a d c d d"
string_array = string_part.split()
#print(string_array)
string_dict = dict()
zero = " "
for i in string_array:
    if i in string_dict:
        string_dict[i] += 1
        zero += f" {i}_{string_dict[i]}"
    else:
        string_dict[i] = 0
        zero += f" {i}"
print(zero)