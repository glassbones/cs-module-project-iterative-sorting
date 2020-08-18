def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)): 
        if arr[i] == target: return i 
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while (left <= right): 
        mid = round(left + (( right-left)/2))       #get halfway point
        if (arr[mid] == target): return mid         #if halfway is target return index
        elif (target < arr[mid]): right = mid - 1   #if target is less than mid, mid is now the new right
        else: left = mid + 1                        #if target is greater than mid, mid is not the new left 
    return -1
