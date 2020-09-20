n=int(input())
for i in range(0,n+1):
  for j in range(i+1,n+1):
    print(j,end=' ')
  print("\r")

#Output- 6
1 2 3 4 5 6 
2 3 4 5 6 
3 4 5 6 
4 5 6 
5 6 
6 
