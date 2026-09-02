students = [{"name": "Tom", "score": 85},{"name": "Jack", "score": 55}, {"name": "Lucy", "score": 92}]
count=0
all=0
total=0
for student in students:
    all=all+1
    total=total+student["score"]

    if student["score"] >= 60:
        print(student["name"],"pass")
        count=count+1
    else:
        print(student["name"],"fail")
    average=total/all

print(count)
print(all)
print(total)
print(average)
        