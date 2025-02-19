def fibo(num):
    if num<=1:
        return num
    else:
        return  fibo(num-1)+fibo(num-2)
num=int(input("enter the number"))
result=fibo(num)
print("fibonciee sum of this number is =",result)