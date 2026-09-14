class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            jtarget = (target - nums[i])
            if jtarget in nums:
                for j in range(i+1, len(nums)):
                    if nums[j] == jtarget:
                        return [i,j]




        