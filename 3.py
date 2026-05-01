def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j].lower() > x.lower():
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr

print(insertion_sort(["Banana", "maçã", "Abacaxi"]))