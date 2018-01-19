class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str_ = '1'

        for _ in range(1, n):
            new_str = ''
            count = 1
            char = str_[0]
            for i in range(1, len(str_)):
                if char == str_[i]:
                    count += 1
                else:
                    new_str = new_str + str(count) + char
                    count = 1
                    char = str_[i]
            if count != 0:
                new_str = new_str + str(count) + char

            str_ = new_str

        return str_


s = Solution()
assert s.countAndSay(1) == '1'
assert s.countAndSay(2) == '11'
assert s.countAndSay(3) == '21'
assert s.countAndSay(4) == '1211'
assert s.countAndSay(5) == '111221'
assert s.countAndSay(6) == '312211'
