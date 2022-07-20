class Solution(object):
    
    def longestPalindrome(self, s):
        
        # Concept
        # take the center of the string and compare it's left and right pointer/character
        # if they both are equal move then check max length and repeat this process
        # Note: In Even Cases, the right will be center + 1, and rest is same
        
        subStr = "" # Substring
        maxLength = 0 # will store the length of longest palindrome
        subStr_l, subStr_r = 0, 0
        
        for i in range(len(s)):
            l,r  = i, i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r - l + 1) > maxLength:
                    maxLength = r - l + 1
                    subStr_l = l
                    subStr_r = r
                    # subStr = s[l:r+1]
                    
                l -= 1
                r += 1
            
            # Even length
            l,r  = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r - l + 1) > maxLength:
                    maxLength = r - l + 1
                    subStr_l = l
                    subStr_r = r
                    
                l -= 1
                r += 1
            
        subStr = s[subStr_l:subStr_r+1]
        return subStr

string = "babad"
print("The input string is: ", string)
solution = Solution()
print("Longest Palindromic Substring is: ", solution.longestPalindrome(string))