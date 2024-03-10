#import numpy as np
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Numpy approach
        # h_index = np.zeros(len(citations))
        # citations.sort()

        # for idx, citation in enumerate(citations):
        #     h_index[idx:] += 1

        # h_index = h_index[::-1]
        # result = 0
        # for i in range(len(citations)):
        #     min_citation = min(citations[i], h_index[i])
        #     if h_index[i] >= min_citation:
        #         result = max(result, min_citation)
        #     else:
        #         break

        # O(N) approach
        max_index = len(citations)
        citations.sort()
        for i in citations:
            if i<max_index:
                max_index-=1
            else:
                return max_index
        return max_index