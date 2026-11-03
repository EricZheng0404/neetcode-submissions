class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        my_dict = {}
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            if sort not in my_dict:
                my_dict[sort] = [strs[i]]
            else: my_dict[sort].append(strs[i])
        
        # print("the val is: ", my_dict["act"])
        list_values = [value for value in my_dict.values()] 
        
        return list_values
        