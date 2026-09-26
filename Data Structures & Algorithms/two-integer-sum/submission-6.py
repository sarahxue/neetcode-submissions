class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap to store the numbers we have passed and their index
        seen = {} # store (value, index)

        for i in range(len(nums)):
            if target-nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i

        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        # #one pass solution 
        # #time: O(n) space: O(n)
        # passed = {}

        # for i in range(len(nums)):
        #     if nums[i] in passed:
        #         return [passed[nums[i]],i]
        #     need = target - nums[i]
        #     passed[need] = i