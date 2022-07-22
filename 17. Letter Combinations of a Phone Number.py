class Solution(object):
    def letterCombinations(self, digits):
        # Concept (Recursion)
        # make a decison tree for every digit
        # i.e 23 then 2 will have three node a,b,c
        # in next step, each a,b,c will have d,e,f
        
        res = []
        digitsToChar = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
                    '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # taking the every character of a digit and calling backtrack function for them
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        
        return res

digits = "23"

print("Input: ", digits)
solution = Solution()
print("Output: ", solution.letterCombinations(digits))