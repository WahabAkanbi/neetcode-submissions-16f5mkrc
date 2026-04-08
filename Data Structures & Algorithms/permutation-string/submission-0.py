from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        look = Counter(s1)
        window = len(s1)

        if(window > len(s2)):
            return False
        left = 0
        right = window
        current = Counter(s2[left:right])

        if(look == current):
            return True

        #right is the edge of the window
        while right < len(s2):
            #look and get index [0:window]
            new_char = s2[right]
            old_char = s2[left]

            current[old_char] -= 1
            current [new_char] += 1

            if(current[old_char] == 0):
                del current[old_char]


            if(look == current):
                return True
            left += 1
            right += 1

        return False

        