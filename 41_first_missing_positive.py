class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        length = len(nums)
        while idx < length:
            item = nums[idx]
            if item > 0 and item != idx + 1:
                if length >= item != nums[item - 1]:
                    temp = nums[item - 1]
                    nums[item - 1] = item
                    nums[idx] = temp
                else:
                    nums[idx] = 0
                    idx + 1
            else:
                idx += 1

        for idx, num in enumerate(nums):
            if num <= 0:
                return idx + 1

        return length + 1


s = Solution()
assert s.firstMissingPositive([2, 1]) == 3
assert s.firstMissingPositive([1, 1]) == 2
assert s.firstMissingPositive([1]) == 2
assert s.firstMissingPositive([]) == 1
assert s.firstMissingPositive([2]) == 1
assert s.firstMissingPositive([1, 2, 0]) == 3
assert s.firstMissingPositive([3, 4, -1, 1]) == 2
