def merge_sort(v):
    if len(v) <= 1:
        return v

    m = len(v) // 2
    e = merge_sort(v[:m])
    d = merge_sort(v[m:])

    return merge(e, d)

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

    return r + a[i:] + b[j:]

logs = [
    "2024-03-10 12:30:00",
    "2023-01-01 09:00:00",
    "2024-03-10 12:29:59"
]

ordenado = merge_sort(logs)
print(ordenado)