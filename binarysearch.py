def binary_search(ary, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if ary[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(ary, low, mid - 1, x)
        else:
            return binary_search(ary, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
ary = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(ary, 0, len(ary)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")