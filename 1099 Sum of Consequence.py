n=int(input())
p=0
for i in range(n):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    sum=0
    if y>x:
        for j in range(x+1,y):
            if j%2==1:
                sum+=j
    if x>y:
        for k in range(y+1,x):
            if k%2==1:
                sum+=k
    if x==y:
        sum=0
    print(sum)
