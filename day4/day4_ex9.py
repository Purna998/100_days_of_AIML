#Create a program that stores student grades in a dictionary and calculates the average grade

stdname=input("Enter Student Name:")
sub_grades=[]
for i in range(4):
    subject_grade=float(input("Enter your subjects grades:"))
    sub_grades.append(subject_grade)
print(sub_grades)


std_grades={"name":stdname, "sub_grades":sub_grades}

print(std_grades['sub_grades'])
sum=0
count=0
for i in std_grades['sub_grades']:
    sum=sum+i
    count+=1
Average=sum/count
print("Average Grade:",Average)
