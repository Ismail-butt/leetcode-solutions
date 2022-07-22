class Solution(object):
    def romanToInt(self, s):
        # Concept (two pointers, i & i+1)
        # VI, if i value is greater than i + 1, then we will add in result i.e 5 + 1 = 6
        # IV, if i value is smaller than i + 1, then we will subtract in result i.e 5 - 1 = 4

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # for storing the result of last character
        res = roman[s[len(s) - 1]]
        
        for i in range(len(s) - 2, -1, -1):
            # Check if the character at right of current character is bigger or smaller
            if roman[s[i]] >= roman[s[i+1]]:
                res += roman[s[i]]
            else:
                res -= roman[s[i]]
                
        return res

s = "MCMXCIV"

print("Input: ", s)
solution = Solution()
print("Output: ", solution.romanToInt(s))