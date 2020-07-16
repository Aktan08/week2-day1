"""
Дан список целых чисел. Заменить отрицательные на -1, положительные - на число 1, ноль
оставить без изменений.
"""
list_ = [1,3,45,-34,23,13,-33,0,43,232,-4,-55,65,-54]
new_list = []


for lis in list_:
    if lis > 0 :
        new_list.append(1)
    elif lis < 0 :
        new_list.append(-1)
    else :
        new_list.append(0)
         
print (new_list)

