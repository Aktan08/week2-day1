"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей
несколько - выведите первую пару.(input: -1 2 3 -1 -2, output: 2, 3)
"""
list_ = [-2, 2, 3, -1, -2,-2, 2, 2]
spisok = []
spisok1 = []

for string in range(1, len(list_) - 1):
    string1 = list_[string]
    previus_string = list_[string- 1]
    next_string = list_[string + 1]

    if  string > 0 and previus_string > 0: 
        spisok.append(string)
        print(spisok)

        
    elif string < 0 and previus_string < 0: 
        spisok1.append(string)
        print(spisok1)
    