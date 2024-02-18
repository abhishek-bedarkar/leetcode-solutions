class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        fq = defaultdict(int)
        meetings.sort()
        booked, free = [], list(range(n))
        
        for s, e in meetings:
            while booked and booked[0][0] <= s:
                _, room = heappop(booked)
                heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heappush(booked, [e, room])
            else:
                release, room = heappop(booked)
                heappush(booked, [release + e - s, room])
            
            fq[room] += 1

        return max(fq, key=fq.get)
