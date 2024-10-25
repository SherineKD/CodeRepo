##You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
#Examples:
#Input: arr[] = [1, 2, 3, 5]
#Output: 4
#Explanation: All the numbers from 1 to 5 are present except 4.

def findMissingNumber(arr, n):
    
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    missing_number = total_sum - array_sum
    return missing_number

# Example usage
arr = [1, 2, 3, 5]
n = 5 
print(findMissingNumber(arr, n))  
