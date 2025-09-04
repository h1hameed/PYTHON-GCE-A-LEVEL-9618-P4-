def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
    print("Sorted:", insertion_sort(data))
