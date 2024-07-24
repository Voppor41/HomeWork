grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Johnny = grades[0]
Bilbo = grades[1]
Steve = grades[2]
Khendrik = grades[3]
Aaron = grades[4]
count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in Johnny:
    count += i

for j in Bilbo:
    count1 += j

for k in Steve:
    count2 += k

for m in Khendrik:
    count3 += m

for l in Aaron:
    count4 += l

count /= len(grades[0])
count1 /= len(grades[1])
count2 /= len(grades[2])
count3 /= len(grades[3])
count4 /= len(grades[4])

students_list = list(students)
students_dict = {students_list[0]: count,
                students_list[1]: count1,
                students_list[2]: count2,
                 students_list[3]: count3,
                 students_list[4]: count4}
print(students_dict)

