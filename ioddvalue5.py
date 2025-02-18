#WAP to create an integer list of 20 elements increase the odd value element by 5(06/04/24)
n=list(map(int,input("Enter 20 element:").split()))
for i in range(20):
    if i%2!=0:
        n[i]+=5
print(n)