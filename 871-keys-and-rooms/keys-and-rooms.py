class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        
        def dfs(start, keys):
            visited.add(start)

            for key in keys:
                if key not in visited:
                    dfs(key, rooms[key])

        dfs(0, rooms[0])
        return  len(visited) == len(rooms)