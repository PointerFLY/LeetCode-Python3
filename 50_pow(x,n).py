class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1:
            return 1
        elif x == -1:
            return 1 if n % 2 == 0 else -1

        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        # Sqrt((0.00001 / 2))
        threshold = 0.00223

        def power(y, p):
            if p == 1:
                return y

            quotient = int(p / 2)
            reminder = p % 2

            left = power(y, quotient)
            if abs(left) <= threshold:
                return 0
            right = power(y, quotient)
            result = left * right
            if reminder == 1:
                result *= y

            return result

        ret = power(x, n)
        ret = round(ret, 5)

        return ret


s = Solution()
assert s.myPow(13.88514, -4) == 0.00003
assert s.myPow(1, -5) == 1
assert s.myPow(-1, 4) == 1
assert s.myPow(-1, 5) == -1
assert s.myPow(10.23, 0) == 1
assert s.myPow(-2.00000, 2) == 4
assert s.myPow(2.00000, 10) == 1024.00000
assert s.myPow(2.10000, 3) == 9.26100
assert s.myPow(34.00515, -3) == 0.00003
assert s.myPow(-1, 1213132131212) == 1.00000
assert s.myPow(2, -2147483648) == 0.00000
assert s.myPow(0.00001, 2147483131213) == 0.00000
