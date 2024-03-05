class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        cities = [i for i in range(len(isConnected))]

        def dfs(city, neighbour):
                #print("dfs ({} , {})".format(city, neighbour))
                if city in cities:
                    cities.remove(city)
                    for n in neighbour:
                        if n in cities:
                            dfs(n, [cty for cty, i in enumerate(isConnected[n]) if i == 1 and n != cty])
        while cities:
            city = cities[0]
            nbh = [cty for cty, i in enumerate(isConnected[city]) if i == 1 and city != cty]
            #print("city : {} -> neighbour : {}".format(city, nbh))
            provinces += 1
            dfs(city, nbh)

        return provinces
