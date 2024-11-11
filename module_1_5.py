immutable_var = 1, 2, 3, 'string', True, False, [4, 5, 6]
immutable_var[6][1] = True
print(immutable_var)
# При попытке заменить неизменяемый эллемент кортежа программа выдает ошибку.
# Однако при замене эллемента списка, находящегося в составе кортежа программа работает исправно
mutable_list = [1, 2, 3, 4, 5, 6 ]
print(mutable_list)
mutable_list[0:3] = 'a', 'b', 'c', 'd'
print(mutable_list)
mutable_list.append(7)
mutable_list.remove('a')
print(mutable_list)
