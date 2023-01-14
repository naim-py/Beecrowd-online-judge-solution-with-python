max=0
pos=0
for i in range(10):
    n=int(input())
    if n>max:
        max=n
        pos=i
print(max)
print(pos+1)