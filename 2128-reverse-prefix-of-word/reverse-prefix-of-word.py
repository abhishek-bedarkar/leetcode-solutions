class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch in word:
            l = len(word)
            idx = word.index(ch)
            print(idx)

            return word[0:idx+1][::-1] + word[idx+1:l]

        return word
        