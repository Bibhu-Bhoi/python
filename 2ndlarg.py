#wap to find the second largest number in a list containing integer.
num_list = [1,2,3,3,3,4,4]
my_set=set(num_list)
print(my_set)
my_num=list(my_set)
print(my_num)
my_num.sort()
print(my_num[-2])

