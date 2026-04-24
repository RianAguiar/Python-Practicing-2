vetor = [3,6,9,2,1,7,9,2,1,7,0]

def bubble_sort(vetor):
    quantidade = len(vetor)-1
    ordenado = False
    while not ordenado: 
        ordenado = True
        for i in range(quantidade):
            if vetor[i] > vetor[i+1]:
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                print(vetor)
                ordenado = False
    return vetor
bubble_sort(vetor)      
