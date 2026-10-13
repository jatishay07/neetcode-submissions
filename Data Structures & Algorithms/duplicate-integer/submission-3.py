class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenN = set()
        for num in nums:
            if num in seenN:
                return True
            else: 
                seenN.add(num)
        return False