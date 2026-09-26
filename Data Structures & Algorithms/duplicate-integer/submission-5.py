class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store seen values in set

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False