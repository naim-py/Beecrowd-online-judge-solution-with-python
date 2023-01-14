sum=0
count=0
for i in range(6):
        n=float(input())
        if (n>0):
            count+=1
            sum=sum+n
avg=sum/count
print(f'{count} valores positivos')
print(f'{avg:0.1f}')