t=int(input())
for i in range(t):
  string=input()
  c="codeforces"
  count=0
  for j in range (len(string)):
    if string[j]!=c[j]:
     count=count+1
     print(count)