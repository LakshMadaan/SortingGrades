#program to average grades and show maximum and minimum grades and to sort them in ascending order.
from numpy import sort
numGrades=int(input('Please enter the number of grades: '))
grades=[]
Total=0

for i in range(1,numGrades+1,1):
    grade=float(input('Enter your marks: '))
    grades.append(grade)
for i in range(0,numGrades,1):
    Total+=grades[i]
Average=Total/numGrades
print('Average is: ',Average)
print('The maximum grade is',max(grades))
print('The minimum grade is',min(grades))
grades.sort(reverse=False) #False means sorting will be in ascending order and True means descending.

print('The order of grades in ascending order is: ')
for i in range(0,numGrades,1):
    print(grades[i])