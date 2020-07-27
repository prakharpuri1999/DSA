#Binary Search
l1=list(map(int,input().split()))
k=int(input("Enter the number to be searched: "))
beg=0
last=len(l1)-1
mid=0
while beg<=last:
    mid=(beg+last)//2
    if l1[mid]==k:
        print("Element found at position: ",mid+1)
        break
    elif k<l1[mid]:
        last=mid-1
    else:
        beg=mid+1
else:
    print("Element not found")
