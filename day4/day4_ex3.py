# Dictionaries - Unordered and mutable
student={"name":"Alice","age":25,"grade":"A"}

student["subject"]="Math"
student["age"]=32


print(student)
print(student['name'])

del student["subject"]
print(student)

student.pop("grade")
print(student)