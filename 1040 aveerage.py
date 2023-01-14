a,b,c,d=map(float,input().split())
av=((a*2)+(b*3)+(c*4)+(d*1))/10
print(f"Media: {av:.1f}")
if av>=7.0:
    print("Aluno aprovado.")
elif av<5.0:
    print("Aluno reprovado.")
elif av>=5.0 and av<=6.9:
    print("Aluno em exame.")
    e=float(input())
    s=(av+e)/2
    print(f"Nota do exame: {e:.1f}")

    if s>=5.0:
        print("Aluno aprovado.")
    elif s<=4.9:
        print("Aluno reprovado.")
    print(f"Media final: {s:.1f}")
