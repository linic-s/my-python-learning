scores = [85, 92, 67, 78, 96, 73, 88]
p=0
total=0
biggest=0
smallest=10000
for score in scores:
    total=total+score
    if score>=60:
        p=p+1
    if score>=biggest:
        biggest=score
    if score<=smallest:
        smallest=score    
a=round(total/len(scores),2)
print("通过的人有",p,"总分是",total,"平均分是",a,"最高分",biggest,"最低分",smallest)