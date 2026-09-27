class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setnum = set(nums)
        longest = 0
        for n in nums:
            if n-1 in setnum:
                continue
            temp = 1
            while n+temp in setnum:
                temp += 1
            longest = max(longest, temp)
        return longest
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # time O(n), space O(n)
        # setNums = set(nums)
        # longest = 0

        # for n in nums:
        #     # check if n-1 is in set
        #     if (n-1) in setNums:
        #         continue
        #     temp = 1
        #     while (n+temp) in setNums:
        #         temp += 1
        #     longest = max(temp, longest)
        
        # return longest