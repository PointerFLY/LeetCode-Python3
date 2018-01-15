class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True

        length = 1
        factor = 10
        while int(x / factor) != 0:
            factor *= 10
            length += 1

        temp = x
        cur_length = length

        for idx in range(1, int(length / 2) + 1):
            power = 10**(cur_length - idx)

            lowest = int(temp % 10)
            highest = int(temp / power)

            if lowest != highest:
                return False

            temp = int((temp - highest * power))
            temp = int((temp - lowest) / 10)
            cur_length -= 1

        return True


s = Solution()
assert s.isPalindrome(1423241) is True
assert s.isPalindrome(21022) is False
assert s.isPalindrome(-2147483648) is False




