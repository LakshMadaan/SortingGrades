#program to average grades and show maximum and minimum grades and to sort them in ascending order.
# This program is without using any sort() or max(),min() functions.
numGrades=int(input('Please enter the number of grades: '))
grades=[]
Total=0
highGrade=0
lowGrade=100
for i in range(1,numGrades+1,1):
    grade=float(input('Enter your marks: '))
    grades.append(grade)
for i in range(0,numGrades,1):
    Total+=grades[i]
Average=Total/numGrades
print('Average is: ',Average)
for i in range(0,numGrades,1):
    if (grades[i]>highGrade):
        highGrade=grades[i]
print('High grade is: ',highGrade)
for i in range(0,numGrades,1):
    if (grades[i]<lowGrade):
        lowGrade=grades[i]
print('Low grade is: ',lowGrade)
for i in range(0,numGrades-1,1):
    for i in range(0,numGrades-1,1):
        if (grades[i]<grades[i+1]):
            swp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=swp
print('Your sorted grades are: ')
for i in range(0,numGrades,1):
    print(grades[i])