"""Создайте лист из чисел и определите количество четных и не четных."""
list_ = list(range(1,12345))
len_=len(list_)
len_chetnye = len(list_[::2])
len_necetnye = len(list_[2::2])
print(len_chetnye)
print(len_necetnye+1)
