class Solution:

    def get_gcd(self,a,b):
        if a == b:
            return a
        elif a>b:
            return self.get_gcd(a-b,b)
        else:
            return self.get_gcd(a,b-a)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ls = len(str1)
        lt = len(str2)
        gcd = self.get_gcd(ls,lt)
        sub_str = ''

        if gcd < lt:
            i=0
            
            while(i != lt):
                if i == 0:
                    sub_str = str2[i:i+gcd]
                else:
                    if sub_str != str2[i:i+gcd]:
                        return ''
                i += gcd
        else:
            sub_str = str2
        i =0
        while( i < ls):
            if sub_str != str1[i:i+gcd]:
                return ''
            i += gcd

        return sub_str