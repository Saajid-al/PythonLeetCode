class Solution:

    def encode(self, strs: list[str]) -> str:
        res = " "
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res,i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j]) #going all the way from i "the beginning" all the way to index j, NOT including J
            res.append(s[j+1 : j + 1 + length]) 
            i = j+1+length
        return res
    #find index of commas
    #reinsert commas

s = Solution()
print(s.encode(["neet","code","love","you"]))
print(s.decode(["4#neet4#code4#love#3you"]))