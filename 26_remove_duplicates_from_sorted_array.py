class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        idx = 1
        previous = nums[0]
        while idx < len(nums):
            if nums[idx] == previous:
                del nums[idx]
            else:
                previous = nums[idx]
                idx += 1

        return len(nums)


s = Solution()
assert s.removeDuplicates([]) == 0
assert s.removeDuplicates([1, 1, 3, 3]) == 2
assert s.removeDuplicates([1, 1, 2]) == 2

