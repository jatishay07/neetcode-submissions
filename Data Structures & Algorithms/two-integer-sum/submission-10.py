class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        
        for i in range (len(nums)):
            sub = target - nums[i]
            if sub in ans:
                return [ans[sub], i]
            ans[nums[i]] = i