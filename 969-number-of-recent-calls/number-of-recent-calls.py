from collections import deque
class RecentCounter:
    def __init__(self):
       self.counter = 0
       self.queue = deque()

    def ping(self, t: int) -> int:
        if len(self.queue) == 0:
            self.queue.append(t)
            return 1
        else:
            while self.queue and  t-self.queue[0]>3000:
                self.queue.popleft()
            self.queue.append(t)
            return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)