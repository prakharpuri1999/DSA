# Counting the number of pairs with a given sum in a Rotated_Sorted Array
def pairs(arr,n,sum):
    # For finding the index of pivot element which is the largest element of the array
    for i in range(n):
        if arr[i]>arr[i+1]:
            break
    l=(i+1)%n # Index of smallest element
    r=i       # Index of largest element
    cnt=0     #For counting number of pairs
    while(l!=r):
        if arr[l] + arr[r]==sum:
            cnt+=1
            if l==(n+r-1)%n:
                return cnt
            l=(l+1)%n
            r=(r-1+n)%n
        elif arr[l] + arr[r] < sum:
            l=(l+1)%n
        else:
            r=(n+r-1)%n
    return cnt

arr = [11, 15, 6, 7, 9, 10] 
sum = 16
print(pairs(arr,6,16))

