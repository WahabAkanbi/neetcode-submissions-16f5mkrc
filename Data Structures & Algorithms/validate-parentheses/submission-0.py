class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"]": "[", ")": "(", "}" :"{"}
        # stack iterate from the back forward
        stack = []
        for i in range(len(s)):
            if s[i] in dic:
                #if its the closing
                #check the stack at the index 0
                opening = dic[s[i]]
                if(not (len(stack) > 0)):
                    return False
                if (stack[-1] != opening):
                    return False
                else:
                    stack.pop()
            else:
                #add the opening to the stack
                stack.append(s[i])

        if(len(stack) != 0):
            return False
        return True