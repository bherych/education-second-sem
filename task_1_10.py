def reverse(P, m):
    i, j = 0, m - 1
    while i < j:
        P[i], P[j] = P[j], P[i]
        i += 1
        j -= 1

def antylex(P, m, n):
    if m == 1:
        print(P[:n])
    else:
        for i in range(m):
            antylex(P, m - 1, n)
            if i < m - 1:
                P[i], P[m - 1] = P[m - 1], P[i]
                reverse(P, m - 1)

def generate_antylex(n):
    P = list(range(1, n + 1))
    antylex(P, n, n)

def main():
    generate_antylex(3)

main()