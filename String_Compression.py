class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        list1 = []
        list2 = []
        temp = "a"
        counter = 0
        for idx, c in enumerate(chars):
            if(c == temp):
                counter += 1
                if (idx+1 == len(chars)):
                    print("ok ok ")
                    list1.append(chars[idx])
                    list2.append(counter)
                    return list1, list2
            elif (c!= temp):
                list1.append(chars[idx-1])
                list2.append(counter)
                temp = c
                counter = 1




        
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))