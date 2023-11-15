import random


def sort_and_print_matrix(m):

    matrix = [
        [random.randint(1, 50) for _ in range(m)]
        for _ in range(m)]
    print(f"\nМатриця {m}x{m} до сортування:")
    for row in matrix:
        for el in row:
            print(f"{el:3d}", end=" ")
        print()

    col_sums = [sum(row[i] for row in matrix) for i in range(m)]

    for i in range(m - 1):
        for j in range(0, m - i - 1):
            if col_sums[j] > col_sums[j + 1]:
                col_sums[j], col_sums[j + 1] = (col_sums[j + 1], col_sums[j])

                for row in matrix:
                    row[j], row[j + 1] = row[j + 1], row[j]

    for i in range(m):
        if i % 2:
            for j in range(m - 1, 0, -1):
                for k in range(m - 1, m - j - 1, -1):
                    if matrix[k][i] < matrix[k - 1][i]:
                        matrix[k][i], matrix[k - 1][i] = matrix[k - 1][i], matrix[k][i]
        else:
            for j in range(m - 1):
                for k in range(0, m - j - 1):
                    if matrix[k][i] < matrix[k + 1][i]:
                        matrix[k][i], matrix[k + 1][i] = (matrix[k + 1][i], matrix[k][i])

    return matrix, col_sums


def display_matrix_and_sums(matrix, col_sums):
    print("\nВідсортована матриця:")
    for row in matrix:
        for el in row:
            print(f"{el:3d}", end=" ")
        print()

    for c in col_sums:
        print(f"{c:3d}", end=" ")


if __name__ == "__main__":
    size = int(input("Введіть число більше 5:"))
    if size >= 5:
        sorted_matrix, column_sum = sort_and_print_matrix(size)
        display_matrix_and_sums(sorted_matrix, column_sum)
    else:
        print("Число має бути більшим за 5")
