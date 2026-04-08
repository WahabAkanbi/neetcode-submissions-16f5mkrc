class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for index in range(len(strs)):
            sorted_key = sorted(strs[index])
            sorted_key = "".join(sorted_key)
            if(sorted_key in dic):
                dic[sorted_key].append(strs[index])
            else:
                dic[sorted_key] = [strs[index]]
        

        return list(dic.values())


        