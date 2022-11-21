def selection_sort(arr: list) -> list:
    n = len(arr)

    for x in range(n-1):
        indexmin = x
        for y in range(n-x-1):
            if arr[indexmin] > arr[x+y+1]:
                indexmin = x+y+1
        # Swap
        arr[x],arr[indexmin] = arr[indexmin],arr[x]

    return arr

if __name__ == "__main__":
    arr = [10, 5, 32, 49, 12, 13, 8, 27, 21, 17]

    result = selection_sort(arr)

    print(result)