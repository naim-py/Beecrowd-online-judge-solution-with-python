n=int(input())
m=int(n/60)
s=n%60
h=int(m/60)
m=m%60
print(f"{h}:{m}:{s}")
