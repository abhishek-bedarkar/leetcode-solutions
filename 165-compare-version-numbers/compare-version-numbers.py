class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        
        #split numbers
        version1_list = version1.split('.')
        version2_list = version2.split('.')

        result = 0
        # iterate for till both list exist
        while len(version1_list) or len(version2_list):
            
            # get left and right elements
            if version1_list and version2_list:
                left, right = int(version1_list.pop(0)), int(version2_list.pop(0))
            elif version1_list:
                right =0
                left =  int(version1_list.pop(0))
            else:
                left = 0
                right = int(version2_list.pop(0))

            # if large or small return result
            if left > right:
                return 1
            elif left < right:
                return -1

        return result



        