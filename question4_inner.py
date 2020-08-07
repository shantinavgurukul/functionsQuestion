# num=int(input("enter the number="))
def odd_even_num(num):
    i=0
    while(i<num):
        if(i%2==0):
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
num=int(input("enter the number="))
odd_even_num(num)
