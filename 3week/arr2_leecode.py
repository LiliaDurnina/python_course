""" https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array"""


def rotate(matrix: list[list[int]]) -> None:
    for x in range(len(matrix)):
        for y in range(x + 1, len(matrix)):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    print(matrix)
    for y in range(0, len(matrix) // 2):
        for x in range(len(matrix)):
            matrix[x][y], matrix[x][len(matrix) - y - 1] = (
                matrix[x][len(matrix) - y - 1],
                matrix[x][y],
            )

    print(matrix)


rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
