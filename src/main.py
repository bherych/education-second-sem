def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip().split(',')
            matrix.append([int(x) for x in row])
    return matrix

def prim(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    total_weight = 0

    for _ in range(n):
        # Знайдемо острів з мінімальним ребром, що ще не включений
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i

        visited[u] = True
        total_weight += min_edge[u]

        # Оновлюємо ваги для сусідів
        for v in range(n):
            if matrix[u][v] != 0 and not visited[v] and matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]

    return total_weight

if __name__ == '__main__':
    matrix = read_matrix('islands.csv')
    print(prim(matrix))
