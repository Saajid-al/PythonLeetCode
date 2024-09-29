class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                r -=1
            elif currentSum < target:
                l +=1
            else:
                return[l+1, r+1]
        return[]

 
s = Solution()
print(s.twoSum([-5,-3,0,2,4,6,8], 5))