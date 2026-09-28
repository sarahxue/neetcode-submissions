class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, len(chars))
        return longest
        
        
        
        
        
        
        
        
        
        
        
        # # time O(n) space O(m) m = # unique chars in s
        # l = 0
        # length = 0
        # window = {}
        
        # for r in range(len(s)):
        #     if s[r] in window:
        #         # move left boundary right past the duplicate, but not backward
        #         l = max(window[s[r]] + 1, l)
        #     window[s[r]] = r
        #     length = max(length, r-l+1)
        # return length