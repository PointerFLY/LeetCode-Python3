class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = [''] * numRows
        str_idx = 0
        i = 0
        down = True

        while str_idx < len(s):
            rows[i] += s[str_idx]

            if down:
                i += 1
                if i == numRows - 1:
                    down = False
            else:
                i -= 1
                if i == 0:
                    down = True
            str_idx += 1

        str_ = ''
        for row in rows:
            str_ += row

        return str_


s = Solution()
assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert s.convert('AB', 1) == 'AB'