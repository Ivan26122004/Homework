grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(type(grades[4][4]))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
print(students)
sorted_students = sorted(students)
print(sorted_students)
Average_score = {}
a = 1.0
print(type(a))
for i in range(len(grades)):
    a = sum(grades[i]) / len(grades[i])
    Average_score.update({sorted_students[i] : a})
print(Average_score)