class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        capacity =0
        lf  =len(flowerbed)
        if lf ==1:
            if flowerbed[0] ==0 :
                capacity += 1
        else:
            for i in range(lf): 
                if i == 0 :
                    if  flowerbed[i]==0 and flowerbed[i+1] ==0 :
                        capacity += 1
                        flowerbed[i]=1
                
                if i == lf-1:
                    if flowerbed[lf-2]==0 and flowerbed[lf-1]==0 :
                        flowerbed[lf-1]=1
                        capacity += 1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i] == 0:
                            flowerbed[i]=1
                            capacity += 1
        if capacity >= n :
                return True
        else:
                return False