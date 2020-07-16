"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего
элемента.(input:1, 5, 2, 4, 3 output: 5, 4)
"""



list_ = [1, 5, 2, 4, 3, 7, 6]

for lis in range(len(list_)):

    string = list_ [lis]
    previus_string = list_[lis-1]

    if  string > previus_string :
        
        print(string) 