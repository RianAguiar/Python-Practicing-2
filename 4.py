import random

v = [random.randint(0, 1000) for _ in range(100)]

def bubble(v):
    c = 0
    v = v[:]
    for i in range(len(v)):
        for j in range(len(v)-1):
            c += 1
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    return c


def insertion(v):
    c = 0
    v = v[:]
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            c += 1
            v[j+1] = v[j]
            j -= 1
        c += 1
        v[j+1] = x
    return c

print("Bubble:", bubble(v))
print("Insertion:", insertion(v))