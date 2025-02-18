#wAP to print the second largest and second smallest number in a given list of 10 integer without using sort function(06/04/24)
n=list(map(int,input("Enter 10 elements:").split()))
for i in range(10):
    for j in range(10):
        if n[i]<n[j]:
            n[i],n[j] = n[j],n[i]
print(f"second largest element is:{n[-2]}\nsecond smallest element is:{n[1]}")

