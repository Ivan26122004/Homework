my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
element_of_list = 0
i = -1
while i < len(my_list) - 1:
    i = 1 + i
    element_of_list = my_list[i]
    if element_of_list > 0:
        print(element_of_list)
    elif element_of_list == 0:
        continue
    else:
        break
