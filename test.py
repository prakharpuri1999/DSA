t=int(input())
flag=0
l2=[]
for i in range(t):
    n,s=map(int,input().split())
    l1=list(map(int,input().split()))
    print(l1)
    for j in range(n):
        sum=l1[j]
        if flag:
            break
        for k in range(j+1,n):
            sum+=l1[k]
            if sum==s:
                l2.append([j+1,k+1])
                flag=1
                break
print(l2)
for a in l2:
    print(*a)
            
        