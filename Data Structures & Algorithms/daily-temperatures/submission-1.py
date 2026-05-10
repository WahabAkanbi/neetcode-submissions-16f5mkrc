from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0] * len(temperatures)

        for index, value in enumerate(temperatures):
            if(len(stack) == 0):
                stack.append((value, index))
            else:
                while stack and stack[-1][0] < value:
                #check if top value of stack is smaller than current value
                    prev_val, prev_ind = stack.pop()
                    result[prev_ind] = index - prev_ind
                stack.append((value, index))


        return result


        