def show_student(student):
    print(student)
students = [{"name": "Tom", "score": 85},{"name": "Jack", "score": 55},{"name": "Lucy", "score": 92}]
def input_student():
    student={}
    student["name"]=input("your name?")
    student["score"]=int(input("your score?"))
    students.append(student)
    print(students)
def search_student():
    a=input("student name:")
    found=False
    for student in students:
        if student["name"].lower() == a.lower():
            print(student["name"])
            print(student["score"])
            found=True
            break
    if found==False:
        print("student no found!")
def remove_student():
    b=input("student name:")
    find=True
    for student in students:
        if b.lower()==student["name"].lower():
            students.remove(student)
            find=False
            print("student is removed!")
            break
    if  find:
        print("student is no found!")

def update_student():
    c=input("student name:")
    for student in students:
        if c.lower()==student["name"].lower():
            print(student["name"])
            d=int(input("new score"))
            student["score"]=d
            print(student["score"])
            

print("student system:1. Show students  2. Add student 3.search student 4.remove student 0. Exit")

while True:
    w=int(input("your choose?"))

    if w==1:
        show_student(students)
        
    if w==2:
        input_student()
    if w==3:
        search_student()
    if w==4:
        remove_student()
    if w==5:
        update_student()
    if w==0:
        break
