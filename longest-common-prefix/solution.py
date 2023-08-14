
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:  
        min_length=201
        min_length_index=-1
        if len(strs)==0:
            return ""
        for i in range(0,len(strs)):
            if len(strs[i])<min_length:
                min_length=len(strs[i])
                min_length_index=i
        prefix_length=0
       
        for i in range(0,min_length):
            check_all=False
            for j in range(0,len(strs)):
                if strs[min_length_index][i] != strs[j][i]:
                    check_all=True
            if check_all == True:
                break
            prefix_length += 1
        
        return strs[min_length_index][0:prefix_length]