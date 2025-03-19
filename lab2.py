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
    
   

def max_hamsters(food_per_day, hamsters):
    
    hamsters = merge_sort(hamsters)
            
    left, right = 0, len(hamsters)
    
    def is_feeding_possible(n):
        consumption = quick_sort([h[0] + h[1] * i for i, h in enumerate(hamsters[:n])])
        needed_food = sum(consumption)
        return needed_food <= food_per_day
    
    while left < right:
        mid = (left + right + 1) // 2
        if is_feeding_possible(mid):
            left = mid
        else:
            right = mid - 1
    
    return left