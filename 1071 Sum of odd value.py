sum=0
x=int(input())
y=int(input())
for i in range(x-1,y,-1):
    if i%2==1:
        print(f"Odd Number = {i}")
        sum+=i

print(f"Sum = {sum}")
