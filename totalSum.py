# numbers = [1, 2, 3, 4, 5]
# # Output
# # 15
# index=0
# sum1=0
# while(index<len(numbers)):
#     sum1=sum1+numbers[index]
#     index=index+1
# print("total sum is=",sum1)
numbers = [1, 2, 3, 4, 5]
def my_sum_function(sum):
    index=0
    sum1=0
    while(index<len(numbers)):
        sum1=sum1+numbers[index]
        index=index+1
    return sum1
print(my_sum_function(numbers))









