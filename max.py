students= [{"name": "Tom", "score": 85},{"name": "Jack", "score": 55}, {"name": "Lucy", "score": 92}]
def ansely_st(students):
    max=0
    min_sc=students[0]["score"]
    count=0
    all=0
    total=0
    for student in students:
        all=all+1
        total=total+student["score"]

        if student["score"] >= 60:
            count=count+1
    
        if student["score"]>=max:
            max=student["score"]
            maxpeople=student["name"]
        if student["score"]<=min_sc:
            min_sc=student["score"]
            minpeople=student["name"]
        average=total/all
    print(max,maxpeople)
    print(min_sc,minpeople)
    print(count)
    print(all)
    print(total)
    print(average)
result=ansely_st(students)


