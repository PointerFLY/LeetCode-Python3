class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        head_idx = 0
        longest_length = 0
        cur_length = 0

        for idx, c in enumerate(s):
            old_idx = dic.get(c)
            dic[c] = idx

            if old_idx is not None and old_idx >= head_idx:
                cur_length = idx - head_idx
                if cur_length > longest_length:
                    longest_length = cur_length
                head_idx = old_idx + 1
                cur_length = idx - head_idx + 1  # refresh
            else:
                cur_length += 1  # Special case: tail of String is the longest

        longest_length = max(cur_length, longest_length)

        return longest_length


s = Solution()
assert s.lengthOfLongestSubstring('abba') == 2
assert s.lengthOfLongestSubstring('dvdf') == 3
assert s.lengthOfLongestSubstring('11112') == 2
assert s.lengthOfLongestSubstring('abcabcbb') == 3
assert s.lengthOfLongestSubstring('bbbbb') == 1
assert s.lengthOfLongestSubstring('pwwkew') == 3
