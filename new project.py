def show_student(student):
    print(student)
students = [{"name": "Tom", "score": 85},{"name": "Jack", "score": 55},{"name": "Lucy", "score": 92}]
def input_student():
    student={}
    student["name"]=input("your name?")
    student["score"]=int(input("your score?"))
    students.append(student)
    print(students)

print("student system:1. Show students  2. Add student  0. Exit")

while True:
    w=int(input("your choose?"))

    if w==1:
        show_student(students)
        
    if w==2:
        input_student()
    if w==0:
        break
