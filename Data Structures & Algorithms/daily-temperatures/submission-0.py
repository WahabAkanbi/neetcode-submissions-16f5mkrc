class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)

        for index in range(len(temperatures)):
            item_add = (index, temperatures[index])

            while (len(stack) > 0 ) and (temperatures[index] > stack[-1][1]):
                val = stack.pop()
                result[val[0]] = index - val[0]
            
            stack.append(item_add)
        
        return result



