class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_sorted = sorted(s, reverse=True)
        for i in range(len(s_sorted) - 1, -1, -1):

            if s_sorted[i] == '1':
                s_sorted[i], s_sorted[-1] = s_sorted[-1], s_sorted[i]
                break
        return ''.join(s_sorted)
        