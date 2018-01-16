class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pairs = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        sum_ = 0
        idx = 0
        str_len = len(s)

        while idx < str_len:
            v1 = pairs.get(s[idx])
            v2 = pairs.get(s[idx:idx + 2]) if idx < str_len - 1 else None

            if v2 is not None:
                sum_ += v2
                idx += 1
            else:
                sum_ += v1

            idx += 1

        return sum_


s = Solution()
assert s.romanToInt('MDCCLXXVI') == 1776
assert s.romanToInt('MCMLIV') == 1954
assert s.romanToInt('MCMXC') == 1990
assert s.romanToInt('MMXIV') == 2014