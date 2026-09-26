class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for l in s:
            count[l] = 1 + count.get(l,0)
        for l in t:
            if l not in count:
                return False
            count[l] -= 1
            if count[l] == 0:
                del count[l]
        
        return len(count) == 0
        
        
        
        
        
        
        
        
        # # hashmap for each string solution 
        # if len(s) != len(t):
        #     return False
        
        # #make hasmaps
        # countS, countT = {}, {}
        
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0) #default value returns 0 if not created yet, then add 1
        #     countT[t[i]] = 1 + countT.get(t[i], 0) 

        # for c in countS: 
        #     if countS[c] != countT.get(c,0):
        #         return False
        # return True
        
        # # #brute force sorting solution -> solves in space O(nlogn), time O(n) bc only sort same length
        # # #check for same length first (O(1))
        # # if len(s) != len(t):
        # #     return False 
        # # sorteds = sorted(s)
        # # sortedt = sorted(t)
        # # #check if s equals t
        # # return sorteds == sortedt