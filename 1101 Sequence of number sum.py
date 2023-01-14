
for i in range(3):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    if(a<=0 or b<=0):
        break
    else:
        if a>b and b>0 :
            sum=0
            for j in range(b,a+1):
                sum+=j
                print(j,end=" ")
            print("Sum=",sum)
        if b>a and a>0 :
            sum=0
            for k in range(a,b+1):
                sum+=k
                print(k,end=" ")
            print("Sum=",sum)
