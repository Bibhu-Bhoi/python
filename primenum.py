num=int(input("Enter a number:"))
count=0
i=1
while(i<=num):
    if i%num==0:
        count+=1
        i=i+1
if(count==2):
    print("Entered number is a prime")
else:
    print("Entered number is not a prime")