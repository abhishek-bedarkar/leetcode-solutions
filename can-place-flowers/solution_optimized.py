class Solution:

    def checkCondition(self, n: int, place:int) -> bool:
        if n <= place:
            return True
        else:
            
            return False


    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        place = 0

        if len(flowerbed) == 1:

            if flowerbed[0] == 0:
                place += 1

            if n <= place: 
                    return True
            else: 
                return False

        for i in range(len(flowerbed)):

            if i==0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    place += 1

                    if place >= n:
                        return True
            
            elif i == len(flowerbed) - 1 :
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    place += 1
                    if place >= n:
                        return True   
            else:
                if  flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    place += 1
                

        return self.checkCondition(n, place)