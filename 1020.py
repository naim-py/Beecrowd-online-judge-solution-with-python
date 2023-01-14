n=int(input())
y=int(n/365)
m=n%365
d=m%30
m=int(m/30)

print('%d ano(s)'%y)
print('%d mes(es)'%m)
print('%d dia(s)'%d)