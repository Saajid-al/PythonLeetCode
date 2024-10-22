class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        numbersToRank = {}
        nums = sorted(set(arr))
        rank =1 

        for num in nums:
            numbersToRank[num] = rank
            rank += 1
        

        for i in range(len(arr)):
            arr[i] = numbersToRank[arr[i]]
        
        return arr
s = Solution()
print(s.arrayRankTransform([40,10,20,30]))