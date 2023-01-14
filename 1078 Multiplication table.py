n=int(input())
if n>1 and n<1000:
    for i in range(1,11,+1):
        print(f"{i} x {n} = {i*n}")