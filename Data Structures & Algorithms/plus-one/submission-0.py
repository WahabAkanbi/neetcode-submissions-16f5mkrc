class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ""

        for val in digits:
            num_str += str(val)
        
        plus_val = int(num_str) + 1

        output = []

        for char in str(plus_val):
            output.append(int(char))
        
        return output
        