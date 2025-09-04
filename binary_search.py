def binary_search(arr, target):
    arr.sort()  # Binary search requires sorted array
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == "__main__":
    data = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
    print("Search 13:", binary_search(data, 13))
    print("Search 100:", binary_search(data, 100))
