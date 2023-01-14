count=0
odd=0
positive=0
negative=0
for i in range(5):
    n=int(input())
    if n%2==0:
        count+=1
    if n%2==1:
        odd+=1
    if (n>0):
        positive+=1
    if (n<0):
        negative+=1
print(f"{count} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")
