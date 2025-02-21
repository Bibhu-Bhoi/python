i=int(input("Enter the number:"))
prod=1
while(i>0):
    prod=prod*(i%10)
    i=i//10
print("the product of entered digit is",prod)