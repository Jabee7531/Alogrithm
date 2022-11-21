def bubble_sort(arr: list) -> list:
    temp = 0

    for x in range(len(arr)-1):
        for y in range(len(arr)-x-1):
            if arr[y] > arr [y+1]:
                # temp = arr[y]
                # arr[y] = arr[y+1]
                # arr[y+1] = temp
                arr[y],arr[y+1] = arr[y+1],arr[y]

    return arr

if __name__ == "__main__":
    arr = [7,5,3,1]

    result = bubble_sort(arr)

    print(result)