class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        control = n
        
        while control != 1:
            if control in seen:
                return False

            running_sum = 0

            seen.add(control)
            for char in str(control):
                val = int(char) * int(char)
                running_sum += val

            control = running_sum

        return True


        