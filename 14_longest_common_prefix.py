class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        prefix = strs.pop()
        while strs:
            str_ = strs.pop()
            min_length = min(len(prefix), len(str_))
            for idx in range(0, min_length):
                if prefix[idx] != str_[idx]:
                    prefix = prefix[0:idx]
                    break
            # When len(str) < len(prefix) && passed for-loop conditions
            prefix = prefix[0:min(len(prefix), min_length)]

        return prefix

s = Solution()
strs1 = ['aaa', 'aa', 'aaa']
strs2 = ['', 'b']
assert s.longestCommonPrefix(strs1) == 'aa'
assert s.longestCommonPrefix(strs2) == ''
