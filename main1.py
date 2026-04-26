student = {'name':'Penguin', 'age':12, 'country':'antarctica'}
print(student)

print("===next===")
print(student['name'])
print("===next===")
print(student.get('name'))
print("===next===")
print(student.get('grade'))
print("===next===")
print(f"my name is {student.get('name')}, I am {student.get('age')} years old")
print("===next===")
student["grade"] = 5
student['gender'] = 'male'
print(student)
