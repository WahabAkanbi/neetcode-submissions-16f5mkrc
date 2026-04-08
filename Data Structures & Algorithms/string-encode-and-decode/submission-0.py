class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for var in strs:
            computed_len = len(var)
            new_str = new_str + str(computed_len) + "#" + var
        
        return new_str

    def decode(self, s: str) -> List[str]:
        # isdigit()
        output = []
        length = len(s)
        i=0

        while i < length:
            j = i

            while s[j] != '#':
                j += 1
            
            word_len = int(s[i:j])
            start_idx = j + 1
            word = s[start_idx: start_idx + word_len]
            output.append(word)
            i = start_idx + word_len
        return output

