class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        maps = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

        roman_str = ''
        factor = 1
        while int(num / factor) >= 1:
            next_num = int(num % (factor * 10) - num % factor)
            char = maps.get(next_num)

            if char is None:
                unit_2 = factor
                unit_1 = unit_2 * 5
                if next_num > unit_1:
                    count = int((next_num - unit_1) / unit_2)
                    char = maps.get(unit_1) + count * maps.get(unit_2)
                else:
                    count = int(next_num / unit_2)
                    char = count * maps.get(unit_2)

            roman_str = char + roman_str
            factor *= 10

        return roman_str



s = Solution()
assert s.intToRoman(4) == 'IV'
assert s.intToRoman(1776) == 'MDCCLXXVI'
assert s.intToRoman(1954) == 'MCMLIV'
assert s.intToRoman(1990) == 'MCMXC'
assert s.intToRoman(2014) == 'MMXIV'