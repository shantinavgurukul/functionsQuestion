def my_min_function(shanti):
    num_min=num[0]
    for i in num:
        if(i<num_min):
            num_min=i
    return num_min
num=[3,4,5,32,1,56,12,54,65,128]
print(my_min_function(num))
