array = [1,5,9,32,6,7,9,2,211,6,99,2,1,6,43,2,3,7,8]
def selectionSort(array):
    n = len(array)
    contador = 0  
    for i in range(n-1):
        min_i = i
        for x in range(i+1, n):
            if array[x] < array[min_i]:
                min_i = x
                contador = contador + 1
                print(f"array --> {array}, quantidade de swaps --> {contador}")
        valor_min = array.pop(min_i)
        array.insert(i, valor_min)        
    return 
selectionSort(array)
