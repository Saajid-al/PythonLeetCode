class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        candylist = []
        maxcandies = max(candies)
        for kid in candies:
            if kid + extraCandies >= maxcandies:
                candylist.append(True)
            else:
                candylist.append(False)
        return candylist


s = Solution()

print(s.kidsWithCandies([4,2,1,1,2], 1))