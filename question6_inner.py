def speed_check(speed):
    scrore=speed-70
    point=scrore//5
    if(point>12):
        return (point,"licence suspended")
    elif (speed<=70):
        return("ok")
    elif(speed>70):
        return(point,"this is 70 cross")
speed=int(input("enter the number="))
print(speed_check(speed))
