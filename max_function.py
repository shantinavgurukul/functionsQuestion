
def my_max_function(shanti):
    num_max=num[0]
    for i in num:
        if(i>num_max):
            num_max=i
    return num_max
num=[3,4,5,32,56,12,54,65,128]
print(my_max_function(num))
