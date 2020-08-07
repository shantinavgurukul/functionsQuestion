def check_length(name,name2):
    a=len(name)
    b=len(name2)
    if(a>b):
        return (a,name)
    elif (b<a):
        return (b,name2)
    else:
        return (a,(name),b,(name2))
name=input("enter the name=")
name2=input("enter the name2=")
print(check_length(name,name2))