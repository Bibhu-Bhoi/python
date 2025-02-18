def perfectnum(n):
    if n <= 0:
        return False
    div=0
    for i in range(1,n):
        if n%i==0:
            div+=i

    return div==n
n=int(input("Enter the number:"))
if perfectnum(n):
    print("perfect")
else:
    print("not perfect")

