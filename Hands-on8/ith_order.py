def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickselect(arr, low, high, i):
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    
    k = pivot_index - low + 1
    
    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quickselect(arr, low, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, high, i - k)

def ith_order(arr, i):
    if i < 1 or i > len(arr):
        return None
    return quickselect(arr, 0, len(arr) - 1, i)

# Example:
arr = [4,8,7,10,2]
i = 3
print(f"The {i}th order statistic is: {ith_order(arr, i)}")
