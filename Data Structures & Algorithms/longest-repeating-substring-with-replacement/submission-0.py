class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        max_freq = 0
        left = 0
        max_sub = 0 

        for index in range(len(s)):
            if s[index] in seen:
                seen[s[index]] += 1
            else:
                seen[s[index]] = 1
            
            max_freq = max(max_freq, seen[s[index]])
            #if the difference in len between max freq and index 
            while (((index - left + 1) - max_freq) > k):
                seen[s[left]] -= 1
                left += 1

            max_sub = max(max_sub, (index - left + 1))

        return max_sub
            

