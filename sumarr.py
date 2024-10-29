#Given an integer array arr[]. You need to find and return the maximum sum possible from all the subarrays.

def max_subarray_sum(arr):
    max_sum = arr[0] 
    current_sum = arr[0]  

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i]) 
        max_sum = max(max_sum, current_sum)  
    return max_sum

arr = [1, 2, 3, -2, 5]
print(max_subarray_sum(arr))