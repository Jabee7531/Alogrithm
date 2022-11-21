def bubble_sort(arr: list) -> list:
    n = len(arr)

    for x in range(n-1):
        for y in range(n-1-x):
            if arr[y] > arr [y+1]:
                # Swap
                # temp = arr[y]
                # arr[y] = arr[y+1]
                # arr[y+1] = temp
                arr[y],arr[y+1] = arr[y+1],arr[y]

    return arr

if __name__ == "__main__":
    arr = [10, 5, 32, 49, 12, 13, 8, 27, 21, 17]

    result = bubble_sort(arr)

    print(result)