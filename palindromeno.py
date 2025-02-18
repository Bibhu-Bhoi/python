a=int(input("Enter the number:"))
str_b=str(a)
reverse=str_b[::-1]
reverse_num=int(reverse)
if reverse_num==a:
    print("it is a palindrom number")
else:
        print("its not a palindrom number")

