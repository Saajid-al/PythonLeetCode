from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a") ] += 1

            res[tuple(count)].append(s)
            
        return res.values()
        #[["hat"],["act", "cat"],["stop", "pots", "tops"]]
        
        
s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))