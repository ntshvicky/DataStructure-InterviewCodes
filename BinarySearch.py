def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target is not present in array
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search_iterative(arr, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
