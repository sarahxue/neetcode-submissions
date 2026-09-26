class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each str in strs - store # of each char 
        # - use # chars as key for hashmap, str as val

        res = defaultdict(list)

        for s in strs: 
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())



       
       
       
       
       
       
       
       
       
       
        # # store occurances of chars for each string in array
        # # use array (tuple) as key for hashmap, and the string as value
        # # return values from hashmap as a list
        # # O(n*m) n = avg # chars in string, m = # strings

        # res = defaultdict(list)

        # for s in strs:
        #     count = [0]*26 #count array for each s, one space for each char a-z

        #     for c in s: #each char in string
        #         count[ord(c) - ord("a")] += 1

        #     res[tuple(count)].append(s)
        
        # return list(res.values())