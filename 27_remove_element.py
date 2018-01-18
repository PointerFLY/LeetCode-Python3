class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


s = Solution()
assert s.removeElement([], 1) == 0
assert s.removeElement([3, 1, 3, 2, 2, 3, 3, 3], 3) == 3