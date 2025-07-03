import csv
import sys

def read_adjacency_matrix(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        matrix = []
        for row in reader:
            matrix.append([int(x) if x else 0 for x in row])
        return matrix

def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    min_edge = [sys.maxsize] * n
    min_edge[0] = 0
    total_weight = 0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not selected[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v

        selected[u] = True
        total_weight += min_edge[u]

        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]

    return total_weight

if __name__ == "__main__":
    filename = 'src/islands.csv'
    matrix = read_adjacency_matrix(filename)
    result = prim_mst(matrix)
    print("Мінімальна довжина кабелю:", result)
