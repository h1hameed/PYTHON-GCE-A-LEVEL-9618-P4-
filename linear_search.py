def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False


if __name__ == "__main__":
    data = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
    print("Search 15:", linear_search(data, 15))
    print("Search 99:", linear_search(data, 99))
