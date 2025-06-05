def solve_govern():
    with open("src/govern.in", "r") as f:
        lines = f.readlines()

    graph = {}          
    in_degree = {}      

    for line in lines:
        a, b = line.strip().split()
        if b not in graph:
            graph[b] = []
        graph[b].append(a)

        if a not in in_degree:
            in_degree[a] = 0
        if b not in in_degree:
            in_degree[b] = 0

        in_degree[a] += 1

    queue = []
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    result = []
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        result.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    with open("src/govern.out", "w") as f:
        for name in result:
            f.write(name + "\n")

if __name__ == "__main__":
    solve_govern()
