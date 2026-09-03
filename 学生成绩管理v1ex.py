students = [
    {"name": "Tom", "score": 85},
    {"name": "Jack", "score": 55},
    {"name": "Lucy", "score": 92}
]
def save_students():
    import json
    with open("student.json","w")as file:
        json.dump(students,file)
save_students()