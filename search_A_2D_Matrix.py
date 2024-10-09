class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in matrix: #for every row 
            for index in range(len(row)): #for every element in the row 
                l = 0
                r = len(row) - 1 
                while(l <= r):                    
                    mid = (l + r) // 2
                    if(row[index] == target):
                        return True
                    elif(row[index] < target):
                        l = mid+1
                    else:
                        r = mid-1
        return False 
        
        
s = Solution()
print(s.searchMatrix([[1]], 1))