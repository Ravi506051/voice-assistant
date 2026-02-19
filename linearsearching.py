def linear_search(arr, target):
    """Performs linear search on an array."""
    for i in range(len(arr)):  # Loop through each element
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Example usage
arr = [5, 8, 12, 15, 20, 25]
target = 15
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")
