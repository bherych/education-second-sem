def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def merge(l, r):
    sorted_matrix = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[i][1] <= r[j][1]:
            sorted_matrix.append(l[i])
            i += 1
        
        else:
            sorted_matrix.append(r[j])
            j += 1

    sorted_matrix.extend(l[i:])
    sorted_matrix.extend(r[j:])

    return sorted_matrix

def merge_sort(matrix):
    if len(matrix) <= 1:
        return matrix


    mid = len(matrix)//2
    left_list = merge_sort(matrix[:mid])
    right_list = merge_sort(matrix[mid:])

    return merge(left_list, right_list)
    
def counting_sort(matrix):

    max_value = max(row[1] for row in matrix)
    print("max value")
    print(max_value)
    
    count = [[] for _ in range(max_value + 1)]
    print("count")
    print(count)

    for row in matrix:
        print(count)
        count[row[1]].append(row)
        

    sorted_matrix = []
    for i in count:
        sorted_matrix.extend(i)

    return sorted_matrix
    
def max_hamsters(food_per_day, hamsters):
    
    hamsters = counting_sort(hamsters)
            
    left, right = 0, len(hamsters)
    

    def is_feeding_possible(n):
        consumption = [h[0] + h[1] * (n-1) for h in hamsters[:n]]
        # Замінив і на (n - 1), оскільки нам потрібно множити жадібність на кількість сусідів-хом'яків
        needed_food = sum(consumption)
        return needed_food <= food_per_day
    
    while left < right:
        mid = (left + right + 1) // 2
        if is_feeding_possible(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

print(max_hamsters(32, [[1,2], [3,4], [5,6]]))