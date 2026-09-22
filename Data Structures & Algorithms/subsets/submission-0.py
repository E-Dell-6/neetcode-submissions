# [3] = 3->[0] + [0]
# [2,3] = 2->(3->[0] + [0]) + [0]
# [1,2,3] = 1->(2->(3->[0] + [0]) + [0]) + 2->(3->[0] + [0]) + [0]
# 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = self.recursion(nums)
        return ans

    def recursion(self, nums: List[int]) -> List[List[int]]:
        #base case
        if (len(nums) == 0):
            return [[]]
        rest = self.recursion(nums[1:])
        return [[nums[0]] + i for i in rest] + rest
        

