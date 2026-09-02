scores = [80, 90, 70]
def get_info(*scores):
    total=0
    for score in scores:
        total=total+score
    average=total/len(scores)
    return total,average
x,y=get_info(*scores)
print(x)
print(y)
