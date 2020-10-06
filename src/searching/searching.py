# return the index at which the number is located if True, and return -1 is False  

def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)): 
  
        if arr[i] == target: 
            return i 
  
    return -1   # not found

# Write an iterative implementation of Binary Search
# return the index at which the number is located if True, and return -1 is False   
def binary_search(arr, target):
    arr.sort()
    start = 0
    end = len(arr)-1

    while end >= start:
        # get the middle point
        # if the middle value is the same as target, set found to True
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            return middle_index
        # move start or end index closer to one another, and shrink our search space     
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return -1

arr = [1, 13, 14, 22, 45, 12]

print(linear_search(arr, 14))
print(binary_search(arr, 45))