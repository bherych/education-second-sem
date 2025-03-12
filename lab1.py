def zigzag(matrix):
    if not matrix or not matrix[0]:
        # Введемо кількість рядків матриці
        matrix_row_num = int(input("Enter the number of rows: "))

        # Введемо кількість стовпчиків
        matrix_column_num = int(input("Enter the number of columns: "))

        # Введемо числа матриці
        matrix_numbers = [int(x) for x in input("Enter numbers for the matrix without commas : ").split()]

        # Створимо матрицю
        matrix = [matrix_numbers[i:i + matrix_column_num] for i in range (0, matrix_row_num * matrix_column_num, matrix_column_num)]
    else:
        matrix_row_num, matrix_column_num = len(matrix), len(matrix[0])

    zig_zag = [[] for _ in range(matrix_row_num+matrix_column_num-1)]

    for i in range(matrix_row_num):
        for j in range(matrix_column_num):
            sum = i + j
            if sum % 2 == 0:
                zig_zag[sum].insert(0, matrix[i][j])
            else:
                zig_zag[sum].append(matrix[i][j])

    # Створимо однорідний список
    result = [el for sublist in zig_zag for el in sublist]
    return result

def main():
    
    print(zigzag(None))

main()