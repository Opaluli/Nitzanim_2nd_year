import numpy as np


def stage1():
    matrix = []
    count = 1
    for i in range(13):
        matrix.append([])
        for j in range(13):
            matrix[i].append(count)
            count = count + 1
    print("Stage 1")
    print(np.matrix(matrix))
    return matrix


def stage2(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if column % 2 != 0:
                matrix[row][column] = matrix[row][column] + column
    print("Stage 2")
    print(np.matrix(matrix))
    return matrix


def sum_of_digits(num):
    sum = 0
    while num != 0:
        sum = sum + num % 10
        num = num // 10
    return sum


def stage3(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            matrix[row][column] = sum_of_digits(matrix[row][column])
    print("Stage 3")
    print(np.matrix(matrix))
    return matrix


def stage4(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row % 2 == 0:
                matrix[row][column] = matrix[row][column] + (row * 3)
    print("Stage 4")
    print(np.matrix(matrix))
    return matrix


def mul_and_add(row, column, cell):
    num = row * column + cell
    return num


def stage5(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row < 10:
                matrix[row][column] = mul_and_add(row, column, matrix[row][column])
    print("Stage 5")
    print(np.matrix(matrix))
    return matrix


def stage6(matrix, column):
    first = matrix[0][column]
    for i in range(len(matrix) - 1): 
        matrix[i][column] = matrix[i + 1][column]
    matrix[-1][column] = first
    print("Stage 6")
    print(np.matrix(matrix))
    return matrix


# bonus

def turn_clockwise(matrix):
    if not len(matrix):
        return

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while left < right and top < bottom:
        prev = matrix[top + 1][left]
        for i in range(left, right + 1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr
        top += 1
        for i in range(top, bottom + 1):
            curr = matrix[i][right]
            matrix[i][right] = prev
            prev = curr
        right -= 1
        for i in range(right, left - 1, -1):
            curr = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = curr
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr
        left += 1

    print("Stage 7A")
    print(np.matrix(matrix))

def turn_counter_clockwise(matrix):
    matrix = np.rot90(matrix)
    print("Stage 7B")
    print(np.matrix(matrix))

def main():
    matrix = stage1()
    matrix = stage2(matrix)
    matrix = stage3(matrix)
    matrix = stage4(matrix)
    matrix = stage5(matrix)
    stage6(matrix, 0)
    # bonus
    turn_clockwise(
        [[1, 2],
         [13, 14]]
    )
    turn_counter_clockwise(
        [[1, 2],
         [13, 14]]
    )
    print("nati123")


main()
