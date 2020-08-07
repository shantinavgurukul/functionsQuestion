def calculator(number_x,number_y):
    if sign=="+":
        num_sum=number_x+number_y
        return num_sum
    elif sign=="-":
        sub_num=number_x - number_y
        return sub_num
    elif sign=="%":
        remainder_sum=number_x % number_y
        return remainder_sum
    else:
        divide=number_x / number_y
        return divide
        
    
sign=input("enter the num=")
print (calculator(8,2))
