class Solution:
    def longestPalindrome(self, s: str) -> str:

        strlen = len(s)
        best_palindrome = ""

        def expand(eleft, eright):
            if(eleft < 0) or (eright >= strlen):
                return (None, None)
            if(s[eright] != s[eleft]):
                return (None, None)
    
            left, right = expand(eleft-1, eright+1)
            if(left == None and right == None):
                return eleft, eright
            return (left, right)



        #goal is to go through and make each item the center
        for i in range(0, len(s)):
            #have each item try out as middle:
            #act as odd
            oddleft, oddright = expand(i, i)
            if(len(best_palindrome) < len(s[oddleft:oddright+1])):
                best_palindrome = s[oddleft:oddright+1]
            if(i+1 < len(s)):
                even_left, even_right = expand(i, i+1)
                if(even_left != None and even_right != None):
                    if(len(best_palindrome) < len(s[even_left:even_right+1])):
                        best_palindrome = s[even_left:even_right+1]

        return best_palindrome


        