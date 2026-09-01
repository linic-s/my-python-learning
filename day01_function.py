scores = [85, 92, 67, 78, 96, 73, 88]

def get_total(scores):
    total = 0

    for score in scores:
        total = total + score

    return total

result = get_total(scores)

print(result)
