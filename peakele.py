#Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).
#Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

def findPeakElement(arr):
    n = len(arr)
    
    if n == 1:
        return 0
    
    if arr[0] >= arr[1]:
        return 0
    
    if arr[n - 1] >= arr[n - 2]:
        return n - 1
    
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i
    
    return -1  

def test_peak_element(arr, expected_index):
    result = 1 if findPeakElement(arr) == expected_index else 0
    print(result)

arr = [1, 3, 20, 4, 1, 0]
expected_index = 2  
test_peak_element(arr, expected_index)
