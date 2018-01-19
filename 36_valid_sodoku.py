class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            set1 = set()
            set2 = set()
            for j in range(0, 9):
                item1 = board[i][j]
                item2 = board[j][i]

                if item1 in set1 and item1 != '.':
                    return False
                else:
                    set1.add(item1)

                if item2 in set2 and item2 != '.':
                    return False
                else:
                    set2.add(item2)

                if i % 3 == 0 and j % 3 == 0:
                    set3 = set()
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            item3 = board[x][y]
                            if item3 in set3 and item3 != '.':
                                return False
                            else:
                                set3.add(item3)

        return True


board1 = [[".","8","7","6","5","4","3","2","1"],
         ["2",".",".",".",".",".",".",".","."],
         ["3",".",".",".",".",".",".",".","."],
         ["4",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".",".","."],
         ["6",".",".",".",".",".",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         ["8",".",".",".",".",".",".",".","."],
         ["9",".",".",".",".",".",".",".","."]]
board2 = [[".","2","1",".",".",".",".",".","."],
          [".",".",".",".","6",".",".",".","."],
          [".",".",".",".",".",".","7",".","."],
          [".",".",".",".","5",".",".",".","."],
          [".",".","5",".",".",".",".",".","."],
          [".",".",".",".",".",".","3",".","."],
          [".",".",".",".",".",".",".",".","."],
          ["3",".",".",".","8",".","1",".","."],
          [".",".",".",".",".",".",".",".","8"]]
s = Solution()
assert s.isValidSudoku(board1) is True
assert s.isValidSudoku(board2) is True
