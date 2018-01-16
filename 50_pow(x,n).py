class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        precision = 0.00001
        if x == 1:
            return 1
        elif x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        neg_n = False
        if n < 0:
            n = -n
            neg_n = True

        ret = 1
        # Accelerate by pre-multiply?
        for i in range(0, n):
            ret *= x
            if abs(ret) < precision / 2:
                break
            elif neg_n and abs(ret) > (1 / precision) * 2:
                break

        if neg_n:
            ret = 1 / ret
        ret = round(ret, 5)

        return ret


s = Solution()
assert s.myPow(2, -2147483648) == 0.00000
assert s.myPow(-2.00000, 2) == 4
assert s.myPow(0.00001, 2147483131213) == 0.00000
assert s.myPow(-1.00000, 1213132131212) == 1.00000
assert s.myPow(2.00000, 10) == 1024.00000
assert s.myPow(2.10000, 3) == 9.26100
assert s.myPow(34.00515, -3) == 0.00003
