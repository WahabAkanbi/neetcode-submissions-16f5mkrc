class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "*": "", "0": "+", "#": ""}

        #made the dictionary pair
        result = []

        def recurse(curr_index, curr_string):
            if(curr_index == len(digits)):
                #we got to the end
                if(len(curr_string) > 0):
                    result.append(curr_string)
                return
            
            #find the element at index
            curr_digit = digits[curr_index]
            possible_options = dictionary[curr_digit]

            for index in range(len(possible_options)):
                #add the new letter to curr_string and recurse
                recurse(curr_index+1, curr_string + possible_options[index])
                
        recurse(0, "")
        return result



        



