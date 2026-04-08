class Solution:
    def numDecodings(self, s: str) -> int:
        strlen = len(s)
        memo = {}


        def recurse(index):
            #either its one number or its one and its pair
            #if its one lets take that path
            if(index > strlen):
                return 0

            if(index == strlen):
                return 1
            
            if(s[index] == '0'):
                return 0

            if(index not in memo):
                two_digit_int = int(s[index:index+2])
                memo[index] = recurse(index + 1)
                if((10 <= two_digit_int < 27) and len(s[index:index+2]) == 2):
                    memo[index] += recurse(index+2)


            return memo[index]
        return(recurse(0))
        