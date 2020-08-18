# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(len(arr)):
        min_i=i                                                             # Set first element index to min index
        for j in range(i+1, len(arr)):                                      # loop list until min_i
            if (arr[j] < arr[min_i]): min_i=j                               # if (el < min) el becomes new min_i
        arr[i], arr[min_i] = arr[min_i], arr[i]                             # Swap the minimum element with the first element of the list       
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for revers in range(len(arr)-1,0,-1):                                   #itterate backwards through the list (len(arr)-1), stop before the first number (-1), and decrement -1 def bubble_sort(arr) # a 4 number array will return passnum =(4,3,2,1)
        for i in range(revers):                                             #so if the arr is [3,4,2,1] the for loop 3 times, then 2 times, the 1 time
            if arr[i]>arr[i+1]: arr[i], arr[i+1] = arr[i+1], arr[i]         #if next number is less than current, swap them
    return arr
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
