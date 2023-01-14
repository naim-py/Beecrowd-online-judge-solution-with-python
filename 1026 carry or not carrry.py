while True:
    try:
        list1=input().split()
        a,b=list1
        print(int(a) ^ int(b))
    except:
        break