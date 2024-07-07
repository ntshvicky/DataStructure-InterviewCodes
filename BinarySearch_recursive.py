def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        # If target is smaller, ignore right half
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    else:
        # Target is not present in array
        return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
