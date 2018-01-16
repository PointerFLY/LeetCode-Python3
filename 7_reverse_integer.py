class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_ = 2**31
        flag = 1
        if x < 0:
            x = -x
            flag = -1

        ret = 0
        while x > 0:
            ret *= 10
            ret += x % 10;
            x = int(x / 10)

            if ret > max_:
                return 0

        return flag * ret


s = Solution()
assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(120) == 21
assert s.reverse(1534236469) == 0




