# num=int(input("enter the number="))
def limit(num):
    i=0
    s=0
    while(i<=num):
        if(i%3==0 or i%5==0):
            s=s+i
        i=i+1

    print(s)
num=int(input("enter the number="))
limit(num)