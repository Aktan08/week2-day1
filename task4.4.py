"""
Исходный список содержит положительные и отрицательные числа. Требуется положительные
поместить в один список, а отрицательные - в другой.
"""
list_ = list(range(-10,11))

spisok_1 = []
spisok_2 = []

for lis in list_:
    if lis > 0 :
        spisok_1.append(lis)
    elif lis < 0 :
        spisok_2.append(lis)
         
print (spisok_1)
print (spisok_2)