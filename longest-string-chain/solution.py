class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        max_chain_dic = {}

        for word in words:
            max_chain_dic[word]=1

        words.sort(key=len)

        for word in words:
            for i in range(0,len(word)):
                pred = word[:i] + word[i+1:]

                if pred in words:
                    max_chain_dic[word] = max(max_chain_dic[word], max_chain_dic[pred]+1)

        return max(max_chain_dic.values())