#BINARY SEARCH THAT RETURNS INDEX OF ELEMENT IF PRESENT ELSE -1
def BinarySearch(arr,l,r,x):
    if r >= l:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr,l,mid-1,x)
        else:
            return BinarySearch(arr,mid+1,r,x)
    else:
        return -1
