class dataStructure(object):
    def binarySearch(self, array, target):
        left = 0
        right = len(array)-1

        while(left<=right): 
            mid = (right+left)//2 #getting the middle of the array
            print("mid" , mid, "Val", array[mid], "left :" , left)
            if(array[mid] == target):
                return mid
            elif array[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

s = dataStructure()
print(s.binarySearch([1,4,5,7,9,12,15,18,19,22,25,29,40,50], 12))
