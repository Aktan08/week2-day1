"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого
элемента в списке. Если наибольших элементов несколько, выведите индекс первого из
них.(input: 1, 2, 3, 2, 1 output: 3, 2)
"""
list_ = [1, 5, 2, 4, 3, 7, 6, 1, 2, 3, 4, 5]
max_ = max(list_)
max_index = list_.index(max_)
print(max_,[max_index])
