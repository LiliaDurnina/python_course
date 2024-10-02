""" https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
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
