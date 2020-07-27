#Cyclic Rotation
l1=list(map(int,input().split()))
n=int(input("Enter number of rotations: "))
for i in range(n):
    temp=l1[-1]
    for j in range(len(l1)-1,0,-1):
        l1[j]=l1[j-1]
    l1[0]=temp
print(l1)