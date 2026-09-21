class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if nums[i] > 0:                      
                break
            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            seen = set()                    
            for j in range(i + 1, n):
                target = 0-nums[i] - nums[j]
                if target in seen:
                    triplet = [nums[i], target, nums[j]]
                    if not ans or ans[-1] != triplet:
                        ans.append(triplet)
                seen.add(nums[j])

        return ans