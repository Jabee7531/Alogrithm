def insertion_sort(arr: list) -> list:
    n = len(arr)

    for x in range(1, n):
        target = arr[x]
        i = x
        while i > 0 and arr[i - 1] > target:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = target

    return arr
    
def insertion_sort_swap(arr: list) -> list:
    n = len(arr)

    for x in range(n-1):
        for y in range(x+1):
            if arr[x-y] > arr[x+1-y]:
                arr[x-y],arr[x+1-y]=arr[x+1-y], arr[x-y]
            else:
                break
    return arr

if __name__ == "__main__":
    arr = [10, 5, 32, 49, 12, 13, 8, 27, 21, 17]

    result = insertion_sort(arr)

    print(result)