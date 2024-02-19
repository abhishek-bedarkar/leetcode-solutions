from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # length should be same
        if len(word1) == len(word2):

            # check if every char is present in both words
            if set(word1) == set(word2):
                
                # create hashtable of word and counter
                word1_ctr = {k:v for k,v in sorted(Counter(word1).items(), key=lambda x: x[1])}
                word2_ctr = {k:v for k,v in sorted(Counter(word2).items(), key=lambda x: x[1])}

                # occurence should match irrespective of key
                for v1,v2 in zip(word1_ctr.values(), word2_ctr.values()):
                    if v1 != v2:
                        return False
                return True
       
        return False
        