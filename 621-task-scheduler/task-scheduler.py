from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if n == 0: return len(tasks)
        # ctr = Counter(tasks)
        # result = ""
        
        # while sum(ctr.values()) != 0:
        #     ky = [i for i in ctr.keys() if ctr[i]>0]

        #     found = False
        #     for k in ky:
        #         if len(result)>= n and k not in result[-n:]:
        #             result += k
        #             ctr[k] -= 1
        #             found = True
        #             break
        #         else:

                
        #     if not found:
        #         result += "0"

        # print(result)
        # return len(result)
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)



                    


        