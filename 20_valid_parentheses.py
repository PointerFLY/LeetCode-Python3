class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        pairs = {'[': ']', '(': ')', '{': '}'}
        for c in s:
            if c in pairs.keys():
                stack.append(c)

            if c in pairs.values():
                if stack and pairs[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return not stack


s = Solution()
assert s.isValid(')({(})') is False
assert s.isValid('3234({23([1231])34})') is True
assert s.isValid('3234({23([1231])34)') is False
