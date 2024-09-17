class Solution(object):
    def topKFrequent(self, nums, k):
        
        count = {}
        freq = [[]for i in range(len(nums) + 1 )] # why the + 1 ? 

        for n in nums:
            count[n] = 1+count.get(n, 0) #
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 

        #another solution, can study this one later, i should've done this bro
        #set_nums = list(set(nums))
        #set_nums = sorted(set_nums, key = lambda x: nums.count(x), reverse = True)

        #return set_nums[:k]



s = Solution()
print(s.topKFrequent([1,2,6,6,6,4,3,1], 2))


#we have a list
#what do we do
# go through the list and count the number of occurences
# {2:1, 2:1, 2:6
# 
# return  