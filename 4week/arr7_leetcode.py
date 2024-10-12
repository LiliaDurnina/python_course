"""https://leetcode.com/problems/spiral-matrix-ii/description/?envType=problem-list-v2&envId=array"""


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [0] * n
        for i in range(n):
            print(i)
            matrix[i] = [0] * n

        left = len(matrix)
        up, right, k = 0, 0, 0
        down = len(matrix[0])
        cur = 1

        while cur <= n * n:
            k += 1
            if k % 4 == 1:
                for y in range(up, down):
                    matrix[right][y] = cur
                    cur += 1
            if k % 4 == 2:
                for x in range(right + 1, left):
                    matrix[x][down - 1] = cur
                    cur += 1
            if k % 4 == 3:
                for y in range(down - 2, up - 1, -1):
                    matrix[left - 1][y] = cur
                    cur += 1

            if k % 4 == 0:
                for x in range(left - 2, right, -1):
                    matrix[x][up] = cur
                    cur += 1

                left -= 1
                right += 1
                up += 1
                down -= 1
        print(matrix)

        return matrix
