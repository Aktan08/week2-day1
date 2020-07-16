"""Дан список. Разрежьте ее на две равные части (если длина списка — четная, а если длина строки
нечетная, то длина первой части должна быть на один символ больше). Переставьте эти две
части местами, результат запишите в новый список и выведите на экран."""


list_ = ["1","2","3","4","5","6","7","8"]
print(len(list_))

if len(list_)%2 == 0 :

    len_ =len(list_)
    half_len = len_/2  # вывод 3.0

    first_half = int(half_len) # = 3
    second_half = int(half_len + half_len) # = 3 + 3 = 6

    new_list = list_[first_half:second_half] + list_[:first_half]
else :
    len_ =len(list_)
    half_len = (len_/2)+1
    first_half = int(half_len)
    second_half = int(half_len + half_len)
    new_list = list_[first_half:second_half] + list_[:first_half]
print(new_list)
print (half_len)