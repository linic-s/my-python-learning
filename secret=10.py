secret=10
answer=int(input("your answer?"))
if answer>secret:
    print("too big")
elif answer==secret:
    print("right!")
else:
    print("too small")
