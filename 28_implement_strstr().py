class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        length = len(needle)
        for i in range(0, len(haystack) - length + 1):
            match = True
            for j in range(0, length):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1


s = Solution()
assert s.strStr('hello', 'll') == 2
assert s.strStr('aabba', 'bba') == 2
assert s.strStr('', '1') == -1
assert s.strStr('a', 'a') == 0
