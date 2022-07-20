class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # Concept
        # take a 4 num rows example & try to do dry run of it
        # to catch a start character of the row, we have to jump 2 * (numRows - 1)
        # to catch a middle character of the row, we have to do minus 2 in the increment i.e V shape
        
        if numRows == 1: return s
        
        output = ""
        for r in range(numRows):
            # increment/step size for every row to catch the row character like P to A etc
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                output += s[i]    
                if (r > 0 and r < numRows - 1 and i+increment-2*r < len(s)):
                    output += s[i+increment-2*r] # minus 2 for each row to catch middle chars
                    
        
        return output

s = "PAYPALISHIRING"
numRows = 4

print("Input: ", s)
solution = Solution()
print("Output: ", solution.convert(s, numRows))