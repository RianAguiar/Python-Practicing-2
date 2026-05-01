def merge_sort(v):
    print("Dividindo:", v)
    
    if len(v) <= 1:
        return v

    meio = len(v) // 2
    esq = merge_sort(v[:meio])
    dir = merge_sort(v[meio:])

    return merge(esq, dir)

def merge(a, b):
    r = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1

    r += a[i:]
    r += b[j:]
    return r
v = [5, 2, 9, 1, 3]
print("Resultado:", merge_sort(v))