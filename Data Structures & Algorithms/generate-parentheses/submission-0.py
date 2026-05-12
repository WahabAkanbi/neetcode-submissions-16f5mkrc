class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #2 rules
        #opened > closed for us to add a new closed
        result = []

        def recurse(opened, closed, path):
            if(closed == n == opened):
                result.append(path)
                return

            if(opened < n):
                recurse(opened + 1, closed, path + "(")
            
            if(closed < opened and closed < n):
                recurse(opened, closed+ 1, path + ")")

        recurse(0, 0, "")
        return result
        