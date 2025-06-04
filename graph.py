def read_matrix(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.strip().split())) for line in file]
    return matrix

def build_graph(matrix):
    rows, cols = len(matrix), len(matrix[0])
    graph = {}

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                neighbors = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 1:
                        neighbors.append((ni, nj))
                graph[(i, j)] = neighbors
    return graph

def bfs_shortest_path(graph, start_nodes, target_col):
    visited = set()
    queue = []
    head = 0

    for r, c in start_nodes:
        if (r, c) in graph:
            queue.append((r, c, 0, [(r, c)])) 
            visited.add((r, c))

    while head < len(queue):
        x, y, dist, path = queue[head]
        head += 1

        if y == target_col:
            return dist, path

        for nx, ny in graph.get((x, y), []):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1, path + [(nx, ny)]))

    return -1, []

def solve():
    matrix = read_matrix("input.txt")
    if not matrix or not matrix[0]:
        result = -1
        path = []
    else:
        rows, cols = len(matrix), len(matrix[0])
        graph = build_graph(matrix)
        start_nodes = [(r, 0) for r in range(rows) if matrix[r][0] == 1]
        result, path = bfs_shortest_path(graph, start_nodes, cols - 1)

    with open("output.txt", "w") as f:
        f.write(str(result) + "\n")
        if path:
            for coord in path:
                f.write(f"{coord[0]},{coord[1]}\n")

if __name__ == "__main__":
    solve()
