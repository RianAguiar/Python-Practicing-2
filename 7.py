jogadores = [
    ("Ana", 100),
    ("Carlos", 200),
    ("Bruno", 100),
    ("Daniel", 150)
]

for i in range(len(jogadores)):
    for j in range(len(jogadores)-1):
        a = jogadores[j]
        b = jogadores[j+1]

        if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
            jogadores[j], jogadores[j+1] = jogadores[j+1], jogadores[j]

print(jogadores)