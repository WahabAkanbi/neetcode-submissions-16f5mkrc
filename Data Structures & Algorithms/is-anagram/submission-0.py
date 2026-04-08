class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for i in range(len(s)):
            if(s[i] in dic):
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        
        for i in range(len(t)):
            if(t[i] in dic):
                dic[t[i]] -= 1
            else:
                return False
        
        for v in dic.values():
            if(v != 0):
                return False
        
        return True

        

        