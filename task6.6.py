"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). Программа
должна быть эффективной и не выполнять лишних действий!
"""
list_ = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]

print(list_)

for index, lis in enumerate(list_,0):
     if index % 2 == 0 :
        print ([index],lis)