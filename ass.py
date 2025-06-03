def bubble_sort_with_output(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Only print if any swap occurred
        if swapped:
            print(f"After iteration {i + 1}: {' '.join(f'{x:.2f}' for x in arr)}")
    # Final sorted output
    print(f"Sorted array: {' '.join(f'{x:.2f}' for x in arr)}")

# Read input
n = int(input())
arr = list(map(float, input().split()))

# Sort and print output
bubble_sort_with_output(arr)