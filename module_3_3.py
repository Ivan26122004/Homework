def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(b = 25)

print_params(c = [1, 2, 3])

print_params()

print_params(a = 12, b = True)

values_list = [11, 'string', True]
values_dict = {'a': 1, 'b': 'String', 'c': False}

print_params(**values_dict)

print_params(*values_list)

values_list_2 = [1, True]

print_params(*values_list_2, 42)
