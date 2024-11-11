#Работа со словарями:
my_dict = {'Ivan' : 19, 'Maksim' : 20}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Alexy'))
my_dict['Vladimir'] = 22
my_dict.update({'Alexander' : 21})
a = my_dict.pop('Ivan')
print(a)
print(my_dict)
#Работа с множествами:
my_set ={2, 3, 2, 'Ivan', 'Alexey', 'Ivan', False, False, True}
print(my_set)
my_set.add(4)
my_set.add(6)
my_set.remove(False)
print(my_set)