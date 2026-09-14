class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = {}

        for n in nums:
            appear[n] = 0

        for n in nums:
            appear[n] += 1

        for n in nums:
            if appear[n] > 1:
                return True

        return False