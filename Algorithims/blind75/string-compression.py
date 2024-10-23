class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0 #to write the compressed chars
        read = 0 #to read through the input array
        while read < len(chars): 
            char = chars[read] 
            count = 0
            
            # Count the occurrences of the current character
            while read < len(chars) and chars[read] == char: 
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
        #go through the loop maybe a while loop, if we encounter a different element. stop. Add the count. and then go through next element.



s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))