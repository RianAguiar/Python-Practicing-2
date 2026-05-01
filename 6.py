def quick_sort(v):
    if len(v) <= 1:
        return v

    pivo = v[-1]
    menores = []
    maiores = []

    for x in v[:-1]:
        if x <= pivo:
            menores.append(x)
        else:
            maiores.append(x)

    print("Pivô:", pivo, "| Menores:", menores, "| Maiores:", maiores)

    return quick_sort(menores) + [pivo] + quick_sort(maiores)


v = [5, 2, 9, 1, 3]
print("Resultado:", quick_sort(v))