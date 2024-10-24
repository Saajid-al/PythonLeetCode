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
        
        
        for idx, val in enumerate(arr):
            arr[idx] = numbersToRank[val]
        return arr


        # for b in arr:
        #     newList.append(hash[b])

        # return newList
        

        #go through each element
        # set the index equal the value
        # the key is the current element
        # for each element in array, we can return our result 


        #remove duplicates



s = Solution()
print(s.arrayRankTransform([40,10,20,30]))