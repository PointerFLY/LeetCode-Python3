class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num > target:
                return max(0, i)

        return len(nums)


s = Solution()
assert s.searchInsert([1, 3, 5, 6], 5) == 2
assert s.searchInsert([1, 3, 5, 6], 2) == 1
assert s.searchInsert([1, 3, 5, 6], 7) == 4
assert s.searchInsert([1, 3, 5, 6], 0) == 0