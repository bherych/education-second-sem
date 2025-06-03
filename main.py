def read_matrix(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.strip().split())) for line in file]
    return matrix

def shortest_path(matrix):
    if not matrix or not matrix[0]:
        return -1

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_path = float('inf')

    for r in range(rows):
        if matrix[r][0] == 1:
            visited = [[False]*cols for _ in range(rows)]
            queue = [(r, 0, 0)]
            visited[r][0] = True
            head = 0

            while head < len(queue):
                x, y, dist = queue[head]
                head += 1

                if y == cols - 1:
                    min_path = min(min_path, dist)
                    break

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if not visited[nx][ny] and matrix[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny, dist + 1))

    return min_path if min_path != float('inf') else -1

if __name__ == "__main__":
    matrix = read_matrix('input.txt')
    result = shortest_path(matrix)
    with open('output.txt', 'w') as file:
        file.write(str(result) + '\n')
    print(result)
