class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Concept
        # Using Sliding Window, we solved this
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

string = "pwwkew"
print("The input string is: ", string)
solution = Solution()
length = solution.lengthOfLongestSubstring(string)
print("The length of the longest non-repeating character substring is: ", length)