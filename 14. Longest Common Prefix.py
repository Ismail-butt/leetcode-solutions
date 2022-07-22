class Solution(object):
    def longestCommonPrefix(self, strs):
        # Concept
        # take the first character of the first element and
        # check if the character is found in other elements of the array or not
        # i == len(s), if we have reached the end of any string, return result
        
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res

strs = ["flower","flow","flight"]

print("Input: ", strs)
solution = Solution()
print("Output: ", solution.longestCommonPrefix(strs))