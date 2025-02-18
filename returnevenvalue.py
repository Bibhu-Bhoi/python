#WAP to create a function that taxes the list as an argument & return the even values of list.print new list with even value(06/04/24)
n=list(map(int,input("Enter the element:").split()))
m=[]
for i in n:
    if i%2==0:
        m.append(i)
print(m)
