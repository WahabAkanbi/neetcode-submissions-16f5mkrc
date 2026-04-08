class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ("+", "-", "*", "/")
        stack = []

        for index, value in enumerate(tokens):
            if(value in operators):
                #order matters
                right = stack.pop()
                left = stack.pop()
                if(value == "+"):
                    output = left + right
                elif(value == "-"):
                    output = left - right
                elif(value == "*"):
                    output = left * right
                elif(value == "/"):
                    output = int(left / right)
                stack.append(output)
            else:
                stack.append(int(value))

        return (stack[0])