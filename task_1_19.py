def generate_partitions(n):
    from copy import deepcopy

    block = [1] * (n + 1)
    direction = [True] * (n + 1)
    next = [0] * (n + 1)
    prev = [0] * (n + 1)

    def print_partition(block):
        blocks = {}
        for i in range(1, n + 1):
            b = block[i]
            if b not in blocks:
                blocks[b] = []
            blocks[b].append(i)
        result = sorted(blocks.values(), key=lambda x: x[0])
        print(result)

    print_partition(block)
    j = n
    while j > 1:
        k = block[j]
        if direction[j]:
            if next[k] == 0:
                next[k] = j
                prev[j] = k
                next[j] = 0
            elif next[k] > j:
                prev[j] = k
                next[j] = next[k]
                prev[next[j]] = j
                next[k] = j
            block[j] = next[k]
        else:
            block[j] = prev[k]
            if k == j:
                if next[k] == 0:
                    next[prev[k]] = 0
                else:
                    next[prev[k]] = next[k]
                    prev[next[k]] = prev[k]
        print_partition(block)
        j = n
        while j > 1 and ((direction[j] and block[j] == j) or (not direction[j] and block[j] == 1)):
            direction[j] = not direction[j]
            j -= 1

def main():
    generate_partitions(4)

main()