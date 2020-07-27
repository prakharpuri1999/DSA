# Searching an element in a Rotated_Sorted array
def search(arr,left,right,target):
    if not arr:
        return -1
    
    if left>right:
        return -1

    mid=(left+right)//2
    if arr[mid]==target:
        return mid+1
    
    # Pivot element is to the right of the middle element
    if arr[mid]>=arr[left]:
        if target>=arr[left] and target<=arr[mid]:
            return search(arr,left,mid-1,target)
        return search(arr,mid+1,right,target)

    # Pivot element is to the left of the middle element
    if target>=arr[mid] and target<=arr[right]:
        return search(arr,mid+1,right,target)
    return search(arr,left,mid-1,target)


print("Element found at position: ", search([4,5,1,2,3],0,4,2))