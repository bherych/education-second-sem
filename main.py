def intersection(set1, set2):
    result = []
    for item in set1:
        for element in set2:
            if item == element:
                result.append(item)
                break
    return result

def cartesian_product(set1, set2):
    result = []
    for item in set1:
        for element in set2:
            result.append((item, element))
    return result

A = list(map(int, input("Перший список: ").split()))
B = list(map(int, input("Другий список: ").split()))

print(intersection(A, B))
print(cartesian_product(A, B))