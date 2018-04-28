class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        permutations = [[None] * len(nums)]
        # For acceleration, sync with permutations
        empty_indices = [set([i for i in range(len(nums))])]

        for idx in range(len(nums) - 1):
            num = nums[idx]
            new_permutations = list()
            new_empty_indices = list()
            for i in range(len(permutations)):
                mutation = permutations[i]
                indices = empty_indices[i]
                for j in indices:
                    new_mutation = list(mutation)
                    new_mutation[j] = num
                    new_indices = set(indices)
                    new_indices.remove(j)
                    # Last iteration can be avoided, since second last iteration means last value is deterministic.
                    if idx == len(nums) - 2:
                        new_mutation[next(iter(new_indices))] = nums[-1]

                    new_permutations.append(new_mutation)
                    new_empty_indices.append(new_indices)

            permutations = new_permutations
            empty_indices = new_empty_indices

        return permutations


s = Solution()
assert s.permute([1]) == [[1]]
assert len(s.permute([1, 2, 3])) == 6
assert len(s.permute([1, 2, 3, 4])) == 24
assert len(s.permute([1, 2, 3, 4, 5])) == 120
