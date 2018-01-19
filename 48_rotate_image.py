class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        size = len(matrix[0])
        max_idx = size - 1

        for j in range(0, int(size / 2)):
            max_i = max_idx - j
            for i in range(j, max_i):
                temp_1 = matrix[i][max_i]
                matrix[i][max_i] = matrix[j][i]

                temp_2 = matrix[max_i][max_i - i + j]
                matrix[max_i][max_i - i + j] = temp_1

                temp_1 = matrix[max_i - i + j][j]
                matrix[max_i - i + j][j] = temp_2

                matrix[j][i] = temp_1


mat_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
ret_1 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
mat_2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
ret_2 = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
mat_3 = []
ret_3 = []
s = Solution()
s.rotate(mat_1)
s.rotate(mat_2)
s.rotate(mat_3)
assert mat_1 == ret_1
assert mat_2 == ret_2
assert mat_3 == ret_3
