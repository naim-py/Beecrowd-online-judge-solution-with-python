import math
a,b,c=map(float,input().split())
d=(b*b)-(4*a*c)
if a==0 or d<0:
    print("Impossivel calcular")
else:
    e=math.sqrt(d)
    R1=(-b+e)/(2*a)
    R2=(-b-e)/(2*a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
