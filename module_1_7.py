grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_abc=sorted(students)
# print(grades)
# print(students_abc)
a=[]
for i in grades:
    a.append(sum(i)/len(i))
# a=(sum(grades[0])/len(grades[0]))
# v_={'students(1)':grades[1]}ocab
# print(a)
b=zip(students_abc,a)
students_gr=dict(b)
print(students_gr)