class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        ret = list()
        for char in digits:
            letters = maps[int(char)]
            if not ret:
                ret = letters
            else:
                temp = ret
                ret = list()
                for idx in range(0, len(temp)):
                    for letter in letters:
                        ret.append(temp[idx] + letter)

        return ret


s = Solution()
assert s.letterCombinations([]) == []
assert s.letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]