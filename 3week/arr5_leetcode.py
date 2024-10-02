"""https://leetcode.com/problems/spiral-matrix/?envType=problem-list-v2&envId=array"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        path = []
        left = len(matrix)
        up, right, k = 0, 0, 0
        down = len(matrix[0])

        while len(path) < (len(matrix) * len(matrix[0])):
            k += 1
            if k % 4 == 1:
                path += [matrix[right][y] for y in range(up, down)]

            if k % 4 == 2:
                path += [matrix[x][down - 1] for x in range(right + 1, left)]
            if k % 4 == 3:
                path += [matrix[left - 1][y] for y in range(down - 2, up - 1, -1)]
            if k % 4 == 0:
                path += [matrix[x][up] for x in range(left - 2, right, -1)]
                left -= 1
                right += 1
                up += 1
                down -= 1
        print(path)

        return path
