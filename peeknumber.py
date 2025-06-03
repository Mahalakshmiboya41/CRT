def find_target_peak(arr, target):
    n = len(arr)
    
    for i in range(n):
        # Check if the current element is equal to target
        if arr[i] == target:
            # Check if it's a peak
            if (i == 0 or arr[i] >= arr[i - 1]) and (i == n - 1 or arr[i] >= arr[i + 1]):
                print(f"Peak element equal to target found at index {i}: {arr[i]}")
                return
    print("Target value is not a peak element.")
arr = [1, 3, 20, 4, 20, 1, 0]
target = 20
find_target_peak(arr, target)