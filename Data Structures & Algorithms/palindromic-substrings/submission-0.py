class Solution:
    def countSubstrings(self, s: str) -> int:

        strlen = len(s)
        odd_pal = 0
        even_pal = 0

        def expand(eleft, eright):
            if(eleft < 0 or eright >= strlen):
                return 0

            if(s[eleft] != s[eright]):
                return 0

            recurse = expand(eleft-1, eright+1)

            return recurse+1

        for i in range(len(s)):
            #odd case

            odd_pal += expand(i, i)

            if(i+ 1 < strlen):
                even_pal += expand(i, i+1)
            
        return (odd_pal + even_pal)
        