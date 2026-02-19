def insertion_sort(arr):
    """Sorts an array using insertion sort."""
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # Current element to insert
        j = i - 1

        # Shift elements of the sorted part to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert element at correct position

# Example usage
arr = [8, 4, 10, 2, 6]
insertion_sort(arr)
print("Sorted array:", arr)
